from abc import ABC, abstractmethod
from rest_framework import status, response
from person.models import RequestResult, RequestStatus


class Mapper(ABC):
    def __init__(self, incoming_data) -> None:
        self._initial = incoming_data

    @abstractmethod    
    def convert(self):
        pass


class ResponseToResultMapper(Mapper):
    def convert(self):
        response_: response.Response = self._initial
        result = RequestResult() 
        if response_.status_code != status.HTTP_201_CREATED:
            result.status = RequestStatus.FAILURE
            result.text = self._get_response_messsage(response_)
        result.status_code = str(response_.status_code)
        result.save()
        return result

    def _get_response_messsage(self, response_: response.Response):
        result = ""
        for value in response_.data:
            error_content = response_.data[value]
            # В ответе может содержаться не только список ошибок,
            # но и только одна строка с ошибкой
            # пример - Невалидный формат входящего json
            if isinstance(error_content, str):
                result += f"{value}: {response_.data[value]}\n"
                continue
            for item in error_content:
                result += f"{value}: {item}\n"
        return result
