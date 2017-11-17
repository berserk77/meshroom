from meshroom.core import desc


class CameraConnection(desc.CommandLineNode):
    internalFolder = '{cache}/{nodeType}/{uid0}/'
    commandLine = 'aliceVision_cameraConnection {allParams}'
    size = desc.DynamicNodeSize('ini')

    inputs = [
        desc.File(
            name="ini",
            label='MVS Configuration file',
            description='',
            value='',
            uid=[0],
            ),
    ]

