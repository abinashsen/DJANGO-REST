import re
import logging

logger = logging.getLogger('django')


class ApiValidations:

    def __init__(self, data):
        self.data = data

    def email_validation(self, email):
        try:
            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if not (re.match(email_regex, email)):
                return "Invalid Email Input ."
            return ""
        except:
            return "email verification has failed."

    def age_validation(self, age):
        try:
            if not (17 >= age >= 15):
                return "age should be between 15 and 17 ."
            return ""
        except:
            return "age verification has failed."

    def submarks_validation(self, submarks):
        try:
            if not (100 >= submarks >= 0):
                return "subject marks should be between 0 and 100."
            return ""
        except:
            return "subject marks verification has failed."

    def totalmarks_validation(self, request_data, totalmarks):
        try:
            calculated_marks = (request_data["flo_marks"] +
                                request_data["sle_marks"] +
                                request_data["tls_marks"] +
                                request_data["mth_marks"] +
                                request_data["gsc_marks"] +
                                request_data["ssc_marks"])
            if not (totalmarks == calculated_marks):
                return "total marks should be equal to sum all subject marks."
            return ""
        except:
            return "total marks verification has failed."

    def validate_data(self):
        try:
            request_data = dict(self.data)
            msg = ""
            for key, value in request_data.items():
                if key == "email":
                    msg += self.email_validation(value)
                if key == "age":
                    msg += self.age_validation(value)

                if key == "flo_marks" or key == "sle_marks" or key == "tls_marks" \
                        or key == "mth_marks" or key == "gsc_marks" or key == "ssc_marks":
                    msg += self.submarks_validation(value)

                if key == "total_marks":
                    msg += self.totalmarks_validation(request_data, value)
            return msg
        except:
            return "whole data verification has failed."
