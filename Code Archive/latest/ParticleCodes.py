#### PDG PARTICLE CODES
####
#### This module contains integer constants which hold the PDG codes for particles. Not all particles 
#### are included. It also contains functions to evaluate whether a particle with a given PDG code
#### belongs to a group of particles like the leptons or quarks.




Collection = {}

QuarkCollection = {}
LeptonCollection = {}

NeutrinoCollection = {}

Collection["DownQuark"] = DownQuark
Collection["UpQuark"] = UpQuark
Collection["StrangeQuark"] = StrangeQuark
Collection["CharmQuark"] = CharmQuark
Collection["BottomQuark"] = BottomQuark
Collection["TopQuark"] = TopQuark
Collection["Photon"] = Photon
Collection["ZZero"] = ZZero
Collection["WPlus"] = WPlus
Collection["WMinus"] = WMinus
Collection["Electron"] = Electron
Collection["AntiElectron"] = AntiElectron
Collection["ElectronNeutrino"] = ElectronNeutrino
Collection["ElectronAntiNeutrino"] = ElectronAntiNeutrino
Collection["MuLepton"] = MuLepton
Collection["AntiMuLepton"] = AntiMuLepton
Collection["MuNeutrino"] = MuNeutrino
Collection["MuAntiNeutrino"] = MuAntiNeutrino
Collection["TauLepton"] = TauLepton
Collection["AntiTauLepton"] = AntiTauLepton
Collection["TauNeutrino"] = TauNeutrino
Collection["TauAntiNeutrino"] = TauAntiNeutrino
Collection["Pi00Meson"] = Pi00Meson
Collection["Pi0Meson"] = Pi0Meson
Collection["Pi1Meson"] = Pi1Meson
Collection["Neutron"] = Neutron
Collection["Proton"] = Proton
Collection["Delta00Baryon"] = Delta00Baryon
Collection["Delta0Baryon"] = Delta0Baryon
Collection["Delta1Baryon"] = Delta1Baryon
Collection["Delta2Baryon"] = Delta2Baryon
Collection["K1Meson"] = K1Meson
Collection["K1AntiMeson"] = K1AntiMeson

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


Names = {}


def ParticleName(Code):
	
	Name = "Unreferenced"
	
	if Code in Names.keys():
		Name = Names[Code]
	
	"""
	for Key1, Code1 in Collection.iteritems():
		if (Code == Code1):
			Name = Key1
	"""	
	return Name


ParticleDictionary = {}

for Variable in dir():

	if (isinstance(eval(Variable), int)):
		ParticleDictionary[eval(Variable)] = Variable
	

