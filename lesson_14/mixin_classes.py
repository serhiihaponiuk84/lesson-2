# Mixin классы - это классы у которых нет данных, но есть методы.
# Mixin используются для добавления одних и тех же методов в разные классы.
#
# В Python примеси делаются с помощью классов.
# Так как в Python нет отдельного типа для примесей, классам-примесям принято давать имена заканчивающиеся на Mixin.
#
# С одной стороны, то же самое можно сделать с помощью наследования обычных классов, но не всегда те методы,
# которые нужны в разных дочерних классах, имеют смысл в родительском.

# class Radio:
#     def play_song(self):
#         pass
#
#     def set_station(self, station):
#         pass
#
#
# class RadioUserMixin(object):
#     def __init__(self):
#         self.radio = Radio()
#
#     def play_song_on_station(self, station):
#         self.radio.set_station(station)
#         self.radio.play_song()
#
#
# class Vehicle:
#     pass
#
#
# class Car(Vehicle, RadioUserMixin):
#     pass

