#!/usr/bin/env python
# Copyright (c) 2022 Lincoln D. Stein (https://github.com/lstein)
# Before running stable-diffusion on an internet-isolated machine,
# run this script from one with internet connectivity. The
# two machines must share a common .cache directory.

import warnings
import load_models

if __name__ == '__main__':
    load_models.main()

