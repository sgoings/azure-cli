# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function
from ..utilities.path import get_repo_root


def get_nose_runner(report_folder, parallel=True, process_timeout=600, process_restart=True):
    """Create a nose execution method"""

    def _run_nose(test_folders):
        import nose
        import os.path

        if not report_folder or not os.path.exists(report_folder) or not os.path.isdir(report_folder):
            raise ValueError('Report folder {} does not exist'.format(report_folder))

        arguments = [__file__, '-v', '-c', os.path.join(get_repo_root(), 'nose.cfg')]
        if parallel:
            arguments += ['--processes=-1', '--process-timeout={}'.format(process_timeout)]
            if process_restart:
                arguments += ['--process-restartworker']

        arguments.extend(test_folders)
        result = nose.run(argv=arguments)

        return result

    return _run_nose
