import re


class TagManipulator():
    def parse_string(self, tags, regex=""):
        result = []

        temp_res = re.split(regex, tags)
        if (len(temp_res[0]) > 0):
            result = temp_res

        trimmed = []
        for item in result:
            trimmed.append(item.strip())
        return trimmed
