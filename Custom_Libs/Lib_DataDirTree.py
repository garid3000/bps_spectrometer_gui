import os
import json
import logging

logger = logging.getLogger(__name__)


class DataDirTree:
    """
    This is class that represents
    data directory and it's files.
    """

    ddir: str = ""
    jpegFnames: list[str] = []
    jpegFnamesFP: list[str] = [] # Full path
    webcamFP: str | None = None
    metajsonText: str = ""
    metajsonFP: str = ""

    def __init__(self) -> None:
        return

    def set_ddir(self, ddir: str) -> bool:
        self.ddir = ddir
        self.jpegFnames = [x for x in os.listdir(self.ddir) if ".jpeg" in x]
        self.jpegFnamesFP = [os.path.join(self.ddir, x) for x in self.jpegFnames]
        # self.webcamFP     = os.path.join(self.ddir, "cam.jpg")
        list_of_jpg_in_ddir: list[str] = [fname_with_jpg for fname_with_jpg in os.listdir(self.ddir) if ((".jpg" in fname_with_jpg) and ("._" not in fname_with_jpg))]
        logger.debug(f"ddir: {list_of_jpg_in_ddir=}")

        if "cam.jpg" in list_of_jpg_in_ddir:
            self.webcamFP = os.path.join(self.ddir, "cam.jpg")
        elif len(list_of_jpg_in_ddir) > 0:
            # if "cam.jpg" isn't exists
            # and there is still .jpg file get the first jpg
            self.webcamFP = os.path.join(self.ddir, list_of_jpg_in_ddir[0])
        else:
            self.webcamFP = None

        logger.debug(f"ddir: {self.webcamFP=}")

        self.metajsonFP = os.path.join(self.ddir, "meta.json")
        self.metajsonText = self.metajson2string()
        return False

    def metajson2string(self) -> str:
        """
        Reads meta.json in directory, prepare for string.
        if it doesn't exist, or problem return some error string
        """
        if not (os.path.isfile(self.metajsonFP)):
            return "Meta data: no file"

        try:
            tmp = open(self.metajsonFP, "r")
            self.meta = json.load(tmp)
            tmp.close()
        except json.JSONDecodeError:
            return "Meta data: bad file format"
        except Exception:
            return "Meta data: failed while reading"

        nf = " not-found"

        return (
            f"Meta data:\n"
            f"- Date: {self.meta['Date' ] if 'Date' in self.meta else nf}\n"
            f"- Time: {self.meta['Time' ] if 'Time' in self.meta else nf}\n"
            f"- GPS : {self.meta['gps'  ] if 'gps'  in self.meta else nf}\n"
            f"- expo: {self.meta['expo' ] if 'expo' in self.meta else nf}\n"
            f"- iso : {self.meta['iso'  ] if 'iso'  in self.meta else nf}\n"
        )

    def directory_structure(self) -> str:
        tmpsubfiles = [x for x in os.listdir(self.ddir)]
        tmpsubfiles.sort()
        return self.ddir + "\n - ".join(tmpsubfiles)
