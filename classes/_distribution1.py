from xcp2k.inputsection import InputSection


class _distribution1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Cost_model = None
        self.Num2d_molecular_distribution = None
        self.Skip_optimization = None
        self.Basic_optimization = None
        self.Basic_spatial_optimization = None
        self.Basic_cluster_optimization = None
        self.Symmetric = None
        self._name = "DISTRIBUTION"
        self._keywords = {'Basic_cluster_optimization': 'BASIC_CLUSTER_OPTIMIZATION', 'Skip_optimization': 'SKIP_OPTIMIZATION', 'Basic_optimization': 'BASIC_OPTIMIZATION', 'Symmetric': 'SYMMETRIC', 'Cost_model': 'COST_MODEL', 'Basic_spatial_optimization': 'BASIC_SPATIAL_OPTIMIZATION', 'Num2d_molecular_distribution': '2D_MOLECULAR_DISTRIBUTION'}

