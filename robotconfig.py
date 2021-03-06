{
    # Class names of motor controllers used.
    # Options:
    # 'Spark'
    # 'Victor'
    # 'VictorSP'
    # 'PWMTalonSRX'
    # 'PWMVictorSPX'
    # 'WPI_TalonSRX'
    # 'WPI_VictorSPX'
    "rightControllerTypes": ["PWMTalonSRX"],
    "leftControllerTypes": ["PWMTalonSRX"],
    # Ports for the left-side motors
    "leftMotorPorts": [7],
    # Ports for the right-side motors
    "rightMotorPorts": [6],
    # Inversions for the left-side motors
    "leftMotorsInverted": [False],
    # Inversions for the right side motors
    "rightMotorsInverted": [True],
    # Wheel diameter (in units of your choice - will dictate units of analysis)
    "wheelDiameter": 0.09,
    # If your robot has only one encoder, remove all of the right enacoder fields
    # Encoder pulses-per-revolution (*NOT* cycles per revolution!)
    # This value should be the pulses per revolution *of the wheels*, and so
    # should take into account gearing between the encoder and the wheels
    "encoderPPR": 112,
    # Ports for the left-side encoder
    "leftEncoderPorts": [0, 1],
    # Ports for the right-side encoder
    "rightEncoderPorts": [2, 3],
    # Whether the left encoder is inverted
    "leftEncoderInverted": True,
    # Whether the right encoder is inverted:
    "rightEncoderInverted": False,
    # Your gyro type (one of "NavX", "Pigeon", "ADXRS450", or "None")
    "gyroType": "ADXRS450",
    # Whatever you put into the constructor of your gyro
    # Could be:
    # "SPI.Port.kMXP" (MXP SPI port for NavX or ADXRS450),
    # "I2C.Port.kOnboard" (Onboard I2C port for NavX)
    # "0" (Pigeon CAN ID),
    # "new TalonSRX(3)" (Pigeon on a Talon SRX),
    # "" (NavX using default SPI, ADXRS450 using onboard CS0, or no gyro)
    "gyroPort": "",
}



