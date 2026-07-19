
# Parent Class: SmartDevice
class SmartDevice:

    #Constructor to initialize every smart devices
    def __init__(self,device_id,name):

        # Private attributes (Encapsulation)
        self.__device_id = device_id
        self.__power_status = False # By default,the device is OFF

        # Public attributes
        self.name = name

    # Getter for device_id
    @property
    def device_id(self):
        return self.__device_id

    #Setter for device_id
    @device_id.setter
    def device_id(self, new_id):
        if new_id.strip() == "":
            print("Device ID cannot be empty")
        else:
            self.__device_id = new_id

    # Getter for power_status
    @property
    def power_status(self):
        return self.__power_status

    # Methods to control power
    def turn_on(self):
        self.__power_status = True
        print(f"The {self.name} is turn ON")

    def turn_off(self):
        self.__power_status = False
        print(f"The {self.name} is turn OFF")

    def display_info(self):
        print(f"Device: {self.name}, ID: {self.__device_id}, Power Status: {'ON' if self.__power_status else 'OFF'}")

# Child Class: TemperatureSensor
class TemperatureSensor(SmartDevice): # child class inheriting from parent class SmartDevice
    def __init__(self, device_id, name, temperature=30):

        # Using super() to initialize parent attributes
        super().__init__(device_id, name)
        self.temperature = temperature    # Additional attribute

    def read_temperature(self):
        print(f"{self.name} Temperature: {self.temperature}°C")

# Class: SecurityCamera
class SecurityCamera(SmartDevice): # child class inheriting from parent class SmartDevice
    def __init__(self, device_id, name,):
        super().__init__(device_id, name)
        self.recording_status = False     # Additional attribute

    def start_recording(self):
        self.recording_status= True
        print(f"{self.name} started recording.")

    def stop_recording(self):
        self.recording_status= False
        print(f"{self.name} stopped recording.")


# Class: SmartLight
class SmartLight(SmartDevice): # child class inheriting from parent class SmartDevice
    def __init__(self, device_id, name, brightness=100):
        super().__init__(device_id, name)
        self.brightness = brightness  # Additional attribute

    # Getter for brightness
    @property
    def brightness(self):
        return self.__brightness

    # Setter with validation (0-100)
    @brightness.setter
    def brightness(self,value):
        if 0 <= value <= 100:
            self.__brightness = value
        else:
            print ("Brightness must be between 0 and 100.")

    def increase_brightness(self):
        if self.__brightness < 100:
            self.__brightness += 10
        print(f"{self.name} Brightness: {self.__brightness}")

    def decrease_brightness(self):
        if self.__brightness > 0:
            self.__brightness -= 10
        print(f"{self.name} Brightness: {self.__brightness}")

# Object Creation
# Creating at least one instance for each class
temp_sensor = TemperatureSensor("TS-112","Living Room Sensor",40)
smart_light = SmartLight("SL-432","Dining Room",80)
sec_camera = SecurityCamera("SC-098 ","Entrance Door Camera",)

# Menu driven Interface
def menu():
    while True:
        print("SMART DEVICE MANAGEMENT SYSTEM MENU")
        print("1. Display Device Information")
        print("2. Turn device On")
        print("3. Turn device Off")
        print("4. Reads temperature")
        print("5. Adjust brightness")
        print("6. Start Recording")
        print("7. Stop Recording")
        print("8. Exit")

        # Ask user to enter a menu option
        choice = input("Enter your choice:")

        # Option 1: Display information for smart devices
        if choice == "1":
            temp_sensor.display_info()
            smart_light.display_info()
            sec_camera.display_info()

        # Option 2: Turn on a selected device
        elif choice == "2":
            # Ask the user which device to turn on
            device = input("Which of the devices? (sensor/light/camera):")
            if device == "sensor": temp_sensor.turn_on()
            elif device == "light": smart_light.turn_on()
            elif device == "camera":sec_camera.turn_on()

         # Option 3: Turn off a selected device
        elif choice == "3":
            device = input("Which of the devices? (sensor/light/camera):")
            if device == "sensor": temp_sensor.turn_off()
            elif device == "light": smart_light.turn_off()
            elif device == "camera":sec_camera.turn_off()

        # Option 4: Read the temperature from the temperature sensor
        elif choice == "4":
            temp_sensor.read_temperature()

        # Option 5: Adjust the smart light brightness
        elif choice == "5":
            # Ask whether to increase or decrease brightness
            action = input("Increase or Decrease brightness? (inc/dec):")
            if action == "inc": smart_light.increase_brightness()
            else: smart_light.decrease_brightness()

        # Option 6: Start recording with the security camera
        elif choice == "6":
            sec_camera.start_recording()

        # Option 7: Stop recording with the security camera
        elif choice == "7":
            sec_camera.stop_recording()

        # Option 8: Exit the smart Device Management system
        elif choice == "8":
            print("Exiting Smart Device Management System")
            break
        # Handle invalid menu choices
        else:
            print("Invalid choice. Try again.")

#  Run the menu function when this file is executed directly
if __name__ == "__main__":
     menu()






