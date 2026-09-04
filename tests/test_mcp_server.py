import importlib.util
import io
import json
import pathlib
import unittest


SERVER_PATH = pathlib.Path(__file__).parents[1] / "mcp-server" / "server.py"
SPEC = importlib.util.spec_from_file_location("chaoyi_mcp_server", SERVER_PATH)
SERVER = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(SERVER)


class StdioFramingTests(unittest.TestCase):
    def test_reads_newline_delimited_json_rpc(self):
        request = {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}
        stream = io.BytesIO(json.dumps(request).encode() + b"\n")

        self.assertEqual(request, SERVER._read_message(stream))

    def test_writes_one_json_rpc_message_per_line(self):
        response = {"jsonrpc": "2.0", "id": 1, "result": {"tools": []}}
        stream = io.BytesIO()

        SERVER._write_message(stream, response)

        self.assertEqual(response, json.loads(stream.getvalue()))
        self.assertTrue(stream.getvalue().endswith(b"\n"))

    def test_lists_all_five_skills(self):
        result, is_error = SERVER._dispatch("tools/list", {})

        self.assertFalse(is_error)
        self.assertEqual(5, len(result["tools"]))


if __name__ == "__main__":
    unittest.main()
