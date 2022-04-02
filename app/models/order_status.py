from enum import Enum


class OrderStatus(str, Enum):
    active = 'ACTIVE'
    hold = 'HOLD'
    archived = 'ARCHIVED'
