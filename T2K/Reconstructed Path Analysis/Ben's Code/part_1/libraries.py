import ROOT

def load(path):
	"""Load the ROOT libraries present at the specified path"""
	ROOT.gSystem.Load(path)

def makeLibraries(filename):
	"""Make libraries based on the contents of the ROOT file specified"""
	tfile = ROOT.TFile(filename, "READ")
	tfile.MakeProject("nd280", "*", "new+")

def main():
	makeLibraries("/storage/physics/phujbk/4_reconstructed_path_analysis/part_1/production5_analysis.root")

if __name__ == "__main__":
        main()
