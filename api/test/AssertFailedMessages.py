from enum import Enum

class AssertFailedMessages(Enum):
    EXPECTED_NOT_FOUND_IN_POST_REGISTER = "Expected results not found in POST \"/register\" endpoint"
    EXPECTED_NOT_FOUND_IN_GET = "Expected results not found in GET \"/users\" endpoint"
