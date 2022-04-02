from enum import Enum


class OrderStatus(str, Enum):
    active = 'active'
    hold = 'hold'
    archived = 'archived'
