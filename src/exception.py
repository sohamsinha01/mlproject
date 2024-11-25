import sys

def error_msg_details(error, error_detail:sys):
    exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_file_name
    error_msg = "Error occured in ppython script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error),

    return error_message
    )

    class CustmException(Exception):
        def __init__(self, error_message, error_detail:sys):
            super().__init__(error_message)
            self.error_message = error_msg_details(error_message, error_detail=error_detail)


        def __str__(self):
            return self.error_message