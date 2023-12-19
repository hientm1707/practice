

# #Send
# #Get data
# from abc import ABC, abstractmethod 


# class BaseService(ABC):
#     _data: dict = None
#     _client = None
#     strategy:str 'DEFAULT'



#     @abstractmethod
#     def set_data(self, data):
#         pass
#     @abstractmethod    
#     def send(self, data):
#         pass

    
#     @property
#     def strategy(name):
#         return self.strategy

#     @strategy.setter
#     def set_strategy(name):
#         self._strategy = name


#     def send():
#         return self._

# class NotificationService(BaseService):


#     def __init__(self, client, data=None):
#         self._client = client
#         if data is not None:
#             self._data = data

#     def set_data(self, data):
#         self._data = data

#     def send(self):
#         self._client.send(self.data)

        

# class EmailService(BaseService):
    

#     def __init__(self, client, data=None)
#         self._client = client
#         if data is not None:
#             self._data = data

#     def send(self):
#         self._client.do_send_email(self.data)
 






# class ServiceFactory():
#     @classmethod
#     def get_service(type:str):
#         if type == 'noti':
#             return NotificationService(client)
#         elif type == 'email':
#             return EmailService()
#         else:
#             raise NotImplementedError("Service is not supported")
        

