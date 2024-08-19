class ClothingBitMask:
    COLORS = {
        "Black": 1 << 0,
        "Red": 1 << 1,
        "Lime": 1 << 2,
        "Blue": 1 << 3,
        "Yellow": 1 << 4,
        "Cyan": 1 << 5,
        "Magenta": 1 << 6,
        "Silver": 1 << 7,
        "Gray": 1 << 8,
        "Maroon": 1 << 9,
        "Olive": 1 << 10,
        "Green": 1 << 11,
        "Purple": 1 << 12,
        "Teal": 1 << 13,
        "Navy": 1 << 14
    }
    
    SIZES = {
        "XS": 1 << 15,
        "S": 1 << 16,
        "M": 1 << 17,
        "L": 1 << 18,
        "XL": 1 << 19,
        "XXL": 1 << 20
    }
    
    MATERIALS = {
        "Cotton": 1 << 21,
        "Polyester": 1 << 22,
        "Linen": 1 << 23,
        "Denim": 1 << 24
    }

    @classmethod
    def export_colors(cls):
        return list(cls.COLORS.keys())

    @classmethod
    def export_sizes(cls):
        return list(cls.SIZES.keys())

    @classmethod
    def export_materials(cls):
        return list(cls.MATERIALS.keys())

    @classmethod
    def add_color(cls, bitmask, color):
        return bitmask | cls.COLORS[color]

    @classmethod
    def add_size(cls, bitmask, size):
        return bitmask | cls.SIZES[size]

    @classmethod
    def add_material(cls, bitmask, material):
        return bitmask | cls.MATERIALS[material]

    @classmethod
    def get_colors(cls, bitmask):
        return [color for color, bit in cls.COLORS.items() if bitmask & bit]

    @classmethod
    def get_sizes(cls, bitmask):
        return [size for size, bit in cls.SIZES.items() if bitmask & bit]

    @classmethod
    def get_materials(cls, bitmask):
        return [material for material, bit in cls.MATERIALS.items() if bitmask & bit]

# Example usage:
# bitmask = 0
# bitmask = ClothingBitMask.add_color(bitmask, "Red")
# bitmask = ClothingBitMask.add_size(bitmask, "M")
# bitmask = ClothingBitMask.add_material(bitmask, "Cotton")

# print(f"Colors: {ClothingBitMask.get_colors(bitmask)}")
# print(f"Sizes: {ClothingBitMask.get_sizes(bitmask)}")
# print(f"Materials: {ClothingBitMask.get_materials(bitmask)}")