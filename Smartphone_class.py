# Assignment 1: Design Your Own Class

# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"📞 Calling {number} from {self.model}...")

    def info(self):
        print(f"{self.brand} {self.model} with {self.storage}GB storage")

# Inherited class (Child)
class CameraPhone(Smartphone):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model, storage)  # Inherit base attributes
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"📸 Taking a photo with {self.camera_megapixels}MP camera!")


# --- Testing the classes ---
phone1 = Smartphone("Samsung", "Galaxy S23", 256)
phone1.info()
phone1.call("08012345678")

print("\n--- Camera Phone ---")
phone2 = CameraPhone("Apple", "iPhone 14", 128, 48)
phone2.info()
phone2.take_photo()