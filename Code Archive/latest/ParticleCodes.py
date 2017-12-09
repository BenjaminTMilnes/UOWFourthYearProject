#### PDG PARTICLE CODES

class Particle(object):
    def __init__(self, code=0, key="", name=""):
        self.code = code
        self.key = key
        self.name = name

    def __str__(self):
        return "{0} ({1})".format(self.name, self.code)


class ParticleCodesReader(object):
    def __init__(self, particle_codes_file="particle_codes.txt"):
        self.particle_codes_file = particle_codes_file

    def get_particles_from_file(self):
        with open(self.particle_codes_file, "r") as f:
            lines = f.readlines()
            particles = self.get_particles_from_lines(lines)

            return particles

    def get_particles_from_lines(self, lines):
        return [self.get_particle_from_line(l) for l in lines]

    def get_particle_from_line(self, line):
        parts = line.split(",")

        particle = Particle()
        particle.code = parts[0].strip()
        particle.key = parts[1].strip()
        particle.name = parts[2].strip()

        return particle


QuarkCollection = {}
LeptonCollection = {}

NeutrinoCollection = {}

QuarkCollection["DownQuark"] = DownQuark
QuarkCollection["UpQuark"] = UpQuark
QuarkCollection["StrangeQuark"] = StrangeQuark
QuarkCollection["CharmQuark"] = CharmQuark
QuarkCollection["BottomQuark"] = BottomQuark
QuarkCollection["TopQuark"] = TopQuark

LeptonCollection["Electron"] = Electron
LeptonCollection["AntiElectron"] = AntiElectron
LeptonCollection["ElectronNeutrino"] = ElectronNeutrino
LeptonCollection["ElectronAntiNeutrino"] = ElectronAntiNeutrino
LeptonCollection["MuLepton"] = MuLepton
LeptonCollection["AntiMuLepton"] = AntiMuLepton
LeptonCollection["MuNeutrino"] = MuNeutrino
LeptonCollection["MuAntiNeutrino"] = MuAntiNeutrino
LeptonCollection["TauLepton"] = TauLepton
LeptonCollection["AntiTauLepton"] = AntiTauLepton
LeptonCollection["TauNeutrino"] = TauNeutrino
LeptonCollection["TauAntiNeutrino"] = TauAntiNeutrino

NeutrinoCollection["ElectronNeutrino"] = ElectronNeutrino
NeutrinoCollection["ElectronAntiNeutrino"] = ElectronAntiNeutrino
NeutrinoCollection["MuNeutrino"] = MuNeutrino
NeutrinoCollection["MuAntiNeutrino"] = MuAntiNeutrino
NeutrinoCollection["TauNeutrino"] = TauNeutrino
NeutrinoCollection["TauAntiNeutrino"] = TauAntiNeutrino


def IsQuark(Code):
    Response = False

    for Code1 in QuarkCollection:
        if (Code1 == Code):
            Response = True

    return Response


def IsLepton(Code):
    Response = False

    for Code1 in LeptonCollection:
        if (Code1 == Code):
            Response = True

    return Response


def IsNeutrino(Code):
    Response = False

    for Code1 in NeutrinoCollection:
        if (Code1 == Code):
            Response = True

    return Response
