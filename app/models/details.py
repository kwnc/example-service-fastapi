from enum import Enum


class OrderStatus(str, Enum):
    active = 'active'
    hold = 'hold'
    archived = 'archived'


class GasolineLevel(str, Enum):
    empty = 'empty'
    quarter = 'quarter'
    half = 'half'
    three_quarters = 'three_quarters'
    full = 'full'
