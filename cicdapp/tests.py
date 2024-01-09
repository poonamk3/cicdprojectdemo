# # from django.test import TestCase

# # Create your tests here.
# import json
# import subprocess

# from django.test import TestCase 

# # class TestForCodeSmell(TestCase):
# # 	def test_with_pylint(self):
# # 		"""run pylint test to ensure code conforms to best practices"""
# # 		print("... testing with pylint ...")
# # 		print("==============================================")


# # 		cmd = ["git", "ls-files", "*.py"]
# # 		output = ""


# # 		with subprocess.Popen(cmd, stdout=subprocess.PIPE) as process:
# # 			output, _ = process.communicate()


# # 		paths = []
# # 		for path in output.splitlines():
# # 			path = path.decode()
# # 			if not re.search(r"(migrations|__init__\.py|apps\.py)", path):
# # 				paths.append(path)


# # 		cmd = [
# # 			"pylint",
# # 			"--output-format",
# # 			"json",
# # 			"--disable",
# # 			"C0114,C0115,C0116,R0903,E0307,E1101,C0103,R1725,R0901,W0221 \
# # 				,W0201,W0212,R0201,C0415,W0614",
# # 		] + paths


# # 		with subprocess.Popen(cmd, stdout=subprocess.PIPE) as process:
# # 			output, _ = process.communicate()
# # 			results = json.loads(output)


# # 		for result in results:
# # 			message_id = result.get("message-id", '').strip()
# # 			message_type = result.get('type', '').upper().strip()
# # 			message = result.get('message', '').replace("\\n", "\n")
# # 			file = result.get("path", '')


# # 			# skip unused import for settings file as it's needed
# # 			ignore_settings_import = ("settings" in file) and (
# # 				message_id in ["W0614", "W0401"]
# # 			)
# # 			ignore_unused_arg = (
# # 				"signals" in file) and (
# # 				message_id == "W0613")


# # 			if not (ignore_settings_import or ignore_unused_arg):
# # 				message = f"""\n({message_id}) {message_type} | {result.get('symbol', '')} on """ \
# # 					f"line {result.get('line', '')} of {file} \n {message}\n"""


# # 				self.assertTrue(message_id == "OK", msg=message) 