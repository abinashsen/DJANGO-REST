import re
import logging

logger = logging.getLogger('django')


# def validate_data(request_data):
#     email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#     msg = ""
#     if not (re.match(email_regex, request_data["email"])):
#         msg += "Invalid Email Input ."+"\n"
#     if not (17 >= request_data["age"] >= 15):
#         msg += "age should be between 15 and 17 ."+"\n"
#     if not ((100, 100, 100, 100, 100, 100) >=
#             (request_data["flo_marks"],
#              request_data["sle_marks"],
#              request_data["tls_marks"],
#              request_data["mth_marks"],
#              request_data["gsc_marks"],
#              request_data["ssc_marks"]) >= (0, 0, 0, 0, 0, 0)):
#         msg += "subject marks should be between 0 and 100."+"\n"
#     if not (request_data["total_marks"] ==
#             (request_data["flo_marks"] +
#              request_data["sle_marks"] +
#              request_data["tls_marks"] +
#              request_data["mth_marks"] +
#              request_data["gsc_marks"] +
#              request_data["ssc_marks"])):
#         msg += "total marks should be equal to sum all subject marks."+"\n"
#
#     return msg


class ApiValidations:

    def __init__(self, data):
        self.data = data

    def email_validation(self, email):
        try:
            logger.info("email validation is called: {} {}".format(email, type(email)))
            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if not (re.match(email_regex, email)):
                return "Invalid Email Input ."
            return ""
        except:
            logger.exception("email validation exception happened")
            return "email varification has failed."

    def age_validation(self, age):
        try:
            logger.info("age validation is called:{} {}".format(age, type(age)))
            if not (17 >= age >= 15):
                return "age should be between 15 and 17 ."
            return ""
        except:
            logger.exception("age validation exception happened")
            return "age varification has failed."

    def submarks_validation(self, submarks):
        try:
            logger.info("submark validation is called:{} ,{}".format(submarks, type(submarks)))
            if not (100 >= submarks >= 0):
                return "subject marks should be between 0 and 100."
            return ""
        except:
            logger.exception("submarks validation exception happened")
            return "subject marks varification has failed."

    def totalmarks_validation(self, request_data, totalmarks):
        try:
            calculated_marks = (int(request_data["flo_marks"][0]) +
                                int(request_data["sle_marks"][0]) +
                                int(request_data["tls_marks"][0]) +
                                int(request_data["mth_marks"][0]) +
                                int(request_data["gsc_marks"][0]) +
                                int(request_data["ssc_marks"][0]))
            logger.info("total mark validation is called: {} ,{}".format(totalmarks, calculated_marks))
            if not (totalmarks == calculated_marks):
                return "total marks should be equal to sum all subject marks."
            return ""
        except:
            logger.exception("total marks validation exception happened")
            return "total marks varification has failed."

    def validate_data(self):
        try:
            logger.info("validate_data validation is called")
            request_data = dict(self.data)
            msg = ""
            for key, value in request_data.items():
                if key == "email":
                    msg += self.email_validation(value[0])
                if key == "age":
                    msg += self.age_validation(int(value[0]))

                if key == "flo_marks" or key == "sle_marks" or key == "tls_marks" \
                        or key == "mth_marks" or key == "gsc_marks" or key == "ssc_marks":
                    msg += self.submarks_validation(int(value[0]))

                if key == "total_marks":
                    msg += self.totalmarks_validation(request_data, int(value[0]))
            return msg
        except:
            logger.exception("whole data validation exception happened")
            return "whole data varification has failed."
