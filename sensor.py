class Sensor:
    def __init__(self, fps, freq, power, min_range, max_range, fov):
        self.fps = fps
        self.frequency = freq
        self.power = power
        self.min_range = min_range
        self.max_range = max_range
        self.azimuth = fov[0]
        self.elevation = fov[1]

class Radar(Sensor):
    def __init__(self, fps, freq, power, min_range, max_range, fov):
        super().__init__(fps, freq, power, min_range, max_range, fov)
        self.frequency = 77e9

class Camera(Sensor):
    def __init__(self, fps, freq, power, min_range, max_range, fov):
        super().__init__(fps, freq, power, min_range, max_range, fov)
        self.type = "Visible"
        self.memory = 1024

class Lidar(Sensor):
    def __init__(self, fps, freq, power, min_range, max_range, fov):
        super().__init__(fps, freq, power, min_range, max_range, fov)
        self.num_of_lights = 8

# Пример использования

Radar_fps = 10
Radar_power = True
Radar_min_range = 0
Radar_max_range = 250
Radar_fov = [70, 10]

camera_fps = 50
camera_power = False
camera_min_range = 0
camera_max_range = 50
camera_fov = [60, 30]

lidar_fps = 20
lidar_power = True
lidar_min_range = 0.5
lidar_max_range = 150
lidar_fov = [360, 20]

my_radar = Radar(Radar_fps,
    None, Radar_power,
    Radar_min_range, 
    Radar_max_range,
    Radar_fov)
print(f'Radar params:\n| power = {Radar_power}\n| min_range = {Radar_min_range}\n| max_range = {Radar_max_range}\n| azimuth = {Radar_fov[0]}\n| elevation = {Radar_fov[1]}\n| frequency = {my_radar.frequency}')

my_camera = Camera(camera_fps, None, camera_power, camera_min_range, camera_max_range, camera_fov)
print(f'Camera params:\n| type = {my_camera.type}\n| memory = {my_camera.memory}\n| power = {camera_power}\n| min_range = {camera_min_range}\n| max_range = {camera_max_range}\n| azimuth = {camera_fov[0]}\n| elevation = {camera_fov[1]}')

my_lidar = Lidar(lidar_fps, None, lidar_power, lidar_min_range, lidar_max_range, lidar_fov)
print(f'Lidar params:\n| num_of_lights = {my_lidar.num_of_lights}\n| power = {lidar_power}\n| min_range = {lidar_min_range}\n| max_range = {lidar_max_range}\n| azimuth = {lidar_fov[0]}\n| elevation = {lidar_fov[1]}')




