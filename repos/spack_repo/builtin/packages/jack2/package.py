# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack_repo.builtin.build_systems.waf import WafPackage

from spack.package import *


class Jack2(WafPackage):
    """JACK Audio Connection Kit (or JACK) is a professional sound server
    API and pair of daemon implementations to provide real-time, low-latency
    connections for both audio and MIDI data between applications."""

    homepage = "https://jackaudio.org"
    git = "https://github.com/jackaudio/jack2.git"

    license("GPL-2.0")
    maintainers("biddisco")

    version("develop", branch="develop")
    version(
        "1.9.22",
        sha256="1e42b9fc4ad7db7befd414d45ab2f8a159c0b30fcd6eee452be662298766a849",
        url="https://github.com/jackaudio/jack2/archive/v1.9.22.tar.gz",
    )

    variant("alsa", default=False, description="Support ALSA driver")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    with when("+alsa"):
        depends_on("alsa-lib")

    def install(self, spec, prefix):
        super().install(spec, prefix)

    def setup_run_environment(self, env):
        # Jack driver directory
        jack_driver_dir = os.path.join(self.prefix.lib, "jack")
        if os.path.exists(jack_driver_dir):
            env.prepend_path("JACK_DRIVER_DIR", jack_driver_dir)
