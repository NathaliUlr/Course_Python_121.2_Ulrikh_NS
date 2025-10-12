from mailing import Mailing  # type: ignore
from address import Address  # type: ignore

from_address = Address('504863', 'Москва', 'Ленина', ' 15', '6')
to_address = Address('625016', 'Тюмень', 'Широтная', ' 61', '82')
cost = 1200
track = 'NS111222333'

delivery_information = Mailing(to_address, from_address, cost, track)

print(delivery_information)
