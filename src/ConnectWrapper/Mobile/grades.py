import requests

class Grades:
    def get_grades(self, **kwargs):
        """
        Mobile.Grades.get_grades

        get_grades is used to get the Connect grades attributed to your specified `token`

        kwargs:
          `token` : string : 36 char (4x'-', 32x'a-z0-9') Example: "55d3d40a-277a-4a69-861d-e2f90144cc62"
        """
        # https://connect.det.wa.edu.au/mobile/api/v1/student/report/assessmentoutlines/DomainConnectUser%3A2514189?_dc=1651238179144
        pass