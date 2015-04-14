import os
import sys
import fnmatch


class FeatureParser(object):
    """
    Parses all feature files in the given directory
    """

    def __init__(self):
        self.write_hnd = None

    def set_up(self):
        """
        Sets up the output file with an rst heading

        :return: None
        """
        heading_text = 'System Features'
        heading_underline = '=' * len(heading_text)
        output_file = '.\\code\\features.rst'
        self.write_hnd = open(output_file, 'w')
        self.write_hnd.write(heading_text + '\n')
        self.write_hnd.write(heading_underline + '\n\n')

    def parse_files(self, dirc):
        """
        Parse the feature files in the given directory

        :param dir: Directory to search in
        :type dir: basestring

        :return: None
        """
        feature_files = []

        #files = os.listdir(dir)
        for root, dirs, files in os.walk(dirc):
            for file in files:
                if fnmatch.fnmatch(file, '*.feature'):
                    feature_files.append(file)

        for feature_file in feature_files:
            if os.path.exists(feature_file):
                f = open(feature_file)
                feature_line = f.readline()  # This should be the feature
                self.write_hnd.write(feature_line)
                self.write_hnd.write('^' * (len(feature_line) - 1) + '\n')

                self.write_hnd.write(f.read())
                self.write_hnd.write('\n\n')
                f.close()

        self.write_hnd.close()

if __name__ == "__main__":
    feature_dir = '..\\behave'  # Used as default

    if len(sys.argv) == 2:
        feature_dir = sys.argv[1]  # If a directory was passed in

    parser = FeatureParser()
    parser.set_up()
    os.chdir(feature_dir)
    parser.parse_files('.')