#
# File containing player logic
#
#

# Dependencies
import random
import string
import json

# Initialise class
class Player:
    # Initialise constructor
    def __init__(self):
        """Read and set default value to config parametes."""
        # Read config file
        file = open("defaultPlayerConfig.json")
        # Parse JSON data
        config = json.load(file)
        # Close file
        file.close()

        # Initialise player id
        self.id = ''.join(random.choice(string.ascii_letters) for i in range(config["idSize"]))

        # Initialise player location
        self.location = config["location"]

        # Initialise hunger status
        self.hunger = config["hunger"]

        # Initialise safety status
        self.safety = config["safety"]

        # Set reproduction chance
        self.reproductionChance = config["reproductionChance"]

        # Set movement limit
        self.movementLimit = config["movementLimit"]

        # Set movement limit mutation chance
        self.movementLimitMutationChance = config["movementLimitMutationChance"]

        # Set vision limit
        self.visionLimit = config["visionLimit"]

        # Set vision limit mutation chance
        self.visionLimitMutationChance = config["visionLimitMutationChance"]

        # Set recharge duration
        self.rechargeDuration = config["rechargeDuration"]

        # Set recharge duration mutation chance
        self.rechargeDurationMutationChance = config["rechargeDurationMutationChance"]

    # Function to get player configuration
    def getConfig(self):
        """Return a dictionary with all player configuration."""
        # Initialise a dictionary
        config = {}
        # Add movement limit
        config["movementLimit"] = self.movementLimit
        # Add vision limit
        config["visionLimit"] = self.visionLimit
        # Add recharge duration
        config["rechargeDuration"] = self.rechargeDuration
        # Return config
        return config

    # Function to update current configuration
    def updateConfig(self, config):
        """Update all configuration using parameter passed.

        Keyword argument:
        config -- dict
        """
        # Check if parameter passed is a dict
        if type(config) == type({}):
            # Check if movement limit is passed
            if "movementLimit" in config.keys():
                # Update movement limit
                self.movementLimit = config["movementLimit"]
            # Check if vision limit is passed
            if "visionLimit" in config.keys():
                # Update vision limit
                self.visionLimit = config["visionLimit"]
            # Check if recharge duration is passed
            if "rechargeDuration" in config.keys():
                # Update recharge duration
                self.rechargeDuration = config["rechargeDuration"]
        # TODO: throw type mismatch error
        # else:

    # Function to update player parameters
    def updateParameters(self):
        """Increment or decrement movement limit, viison limit and recharge duration based on mutation chances."""
        # Roll chances for updating movement limit
        if random.uniform(0, 1) < self.movementLimitMutationChance:
            # Roll chances to decide between incrementation and decrementation
            if random.randint(1, 2)%2 == 0:
                # Increment parameter
                self.movementLimit = self.movementLimit + 1
            else:
                # Decrement parameter
                self.movementLimit = self.movementLimit - 1
        # Roll chances for updating vision limit
        if random.uniform(0, 1) < self.visionLimitMutationChance:
            # Roll chances to decide between incrementation and decrementation
            if random.randint(1, 2)%2 == 0:
                # Increment parameter
                self.visionLimit = self.visionLimit + 1
            else:
                # Decrement parameter
                self.visionLimit = self.visionLimit - 1
        # Roll chances for updating recharge duration
        if random.uniform(0, 1) < self.rechargeDurationMutationChance:
            # Roll chances to decide between incrementation and decrementation
            if random.randint(1, 2)%2 == 0:
                # Increment parameter
                self.rechargeDuration = self.rechargeDuration + 0.1
            else:
                # Decrement parameter
                self.rechargeDuration = self.rechargeDuration - 0.1

    # Function to get player id
    def getId(self):
        """Return player id."""
        return self.id

    # Function to get player location
    def getLocation(self):
        """Return location."""
        return self.location

    # Function to update player location
    def updateLocation(self, location):
        """Set location to given location parameter.

        Keyword arguments:
        location -- tuple
        """
        # Check if location paramenter is a tuple
        if type(location) == type((1,2)):
            # Update location
            self.location = location
        # TODO: throw error (passed parameter is not a tuple)
        # else:

    # Function to get hunger status
    def getHungerStatus(self):
        """Return hunger status."""
        return self.hunger

    # Funtion to update hunger status
    def updateHungerStatus(self, status):
        """Update hunger status to the parameter passed.

        Keyword arguments:
        status -- boolean
        """
        # Check if passed parameter is a boolean
        if type(status) == type(True):
            # Update hunger status
            self.hunger = status
        # TODO: throw error (parameter must be a boolean)
        # else:

    # Function to get safety status
    def getSafetyStatus(self):
        """Return safety status."""
        return self.safety

    # Function to update safety status
    def updateSafetyStatus(self, status):
        """Update safety status to the parameter passed.

        Keyword arguments:
        status -- boolean
        """
        # Check if passed parameter is a boolean
        if type(status) == type(True):
            # Update safety status
            self.safety = status
        # TODO: throw error (parameter must be a boolean)
        # else:

    # Function to get player movement limit
    def getMovementLimit(self):
        """Return movement limit value."""
        return self.movementLimit

    # Function to get player vision limit
    def getVisionLimit(self):
        """Return vision limit value."""
        return self.visionLimit

    # Function to get recharge duration
    def getRechargeDuration(self):
        """Return recharge duration value."""
        return self.rechargeDuration

    # Function to return reproduction chance
    def getReproductionChance(self):
        """Return reproduction chance."""
        return self.reproductionChance

    # Function to update reproduction chance
    def updateReproductionChance(self, action):
        """Increment reproduction chance by 10% or reset reproduction chance to 0 depending on the parameter passed.

        Keyword arguments:
        action -- string in 'increment' or 'reset'
        """
        # Check if action is increment
        if action == "increment":
            # Check if reproduction chance is less than 1
            if self.reproductionChance < 1:
                # Increment reproduction chance
                self.reproductionChance = self.reproductionChance + 0.1
        elif action == "reset":
            # Set reproduction chance to 0
            self.reproductionChance = 0
