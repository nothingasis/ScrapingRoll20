import requests
import os


def download_file(url, filename='', foldername='misc'):
    try:
        if filename:
            filename = filename + '.png'
            pass
        else:
            return "File name required"
        
        if foldername:
            filename = foldername + "/" + filename
            pass

        try:
            os.makedirs(foldername)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None

downloadLink = 'https://s3.amazonaws.com/files.d20.io/marketplace/14665/l6B57dHOGekSHDGEnE4UGg/max.png?1366969146'
download_file(url=downloadLink, filename="image_1", foldername="default")