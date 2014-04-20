import multiprocessing
import os


def GetFlipList(path):
    FlippedSections = list();

    flipFileName = os.path.join(path, 'FlipList.txt');
    if os.path.exists(flipFileName) == False:
        return FlippedSections;

    flipFile = open(flipFileName, 'r');
    lines = flipFile.readlines();
    flipFile.close();

    for line in lines:
        sectionNumber = int(line);
        FlippedSections.append(sectionNumber);

    return FlippedSections;

class __Config:
    '''A place to store hardcoded values used throughout the buildscripts'''


    def __init__(self):
        # Standard format strings
        self.DefaultImageExt = 'png';
        self.TileFormat = 'Tile%06d';
        self.SectionFormat = '04d';
        self.SectionTemplate = '%04d';

        self.LevelFormat = '%03d';

        self.DownsampleFormat = '%03d';
        # self.GridTileCoordFormat = '03d';  #The optimized tile format string
        self.GridTileCoordFormat = '03d';  # The optimized tile format string
        self.GridTileCoordTemplate = '%' + self.GridTileCoordFormat;  # The optimized tile format string
        self.GridTileNameTemplate = '%(prefix)sX%(X)' + self.GridTileCoordFormat + '_Y%(Y)' + self.GridTileCoordFormat + '%(postfix)s';  # The optimized tile format string
        self.GridTileMatchStringTemplate = '%(prefix)sX%(X)s_Y%(Y)s%(postfix)s';  # The optimized tile format string
        self.TileCoordFormat = '%03d';
        self.__NumProcs = None;
        self.DefaultDownsampleLevels = [1, 2, 4, 8, 16, 32, 64, 128];
        self.DebugFast = True;  # Set to true to skip time consuming tests such as bits-per-pixel when debugging.

    @property
    def NumProcs(self):
        '''Return the number of processors'''
        if self.__NumProcs is None:
            import multiprocessing;
            self.__NumProcs = multiprocessing.cpu_count();
            try:

                from Utils import prettyoutput;
                prettyoutput.CurseString("# of Cores", str(self.__NumProcs));
            except:
                pass;

        return self.__NumProcs;

    # Users calling this library can change this list to adjust the downsample levels used

Current = __Config();

