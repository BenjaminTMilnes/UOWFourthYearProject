import libraries
import glob
import sys
import ROOT
import RooTrackerTools
import math

class Analysis:
	
	
	def __init__(self, input_filename_list, output_filename):
		self.input_filename_list = input_filename_list
		self.output_filename = output_filename
		self.histograms = {}
		self.modules = []
		# Load the modules needed in this analysis
		self.basic_header = self.loadModule("HeaderDir/BasicHeader")
		self.genievtx = self.loadModule("TruthDir/GRooTrackerVtx")
		# Declare GRooTrackerTools class instance
		self.Rootools = RooTrackerTools.RooTrackerTools()
		self.ReconDir_Global = self.loadModule("ReconDir/Global")
		self.TruthDir_Vertices = self.loadModule("TruthDir/Vertices")
		self.TruthDir_Trajectories = self.loadModule("TruthDir/Trajectories")
		
		self.FGDProportion=0
		self.TotalVertices=0
		self.FGDNC=0
		self.NCNeutron=0
		self.CCQEFGD=0
		self.CCQEFGDandPID=0
		self.PIDcount=0
		self.PIDProton=0
	
	
	def beforeLoop(self):
		"""Opens input and output files, creates histograms and intitialises any other necessary variables"""
		self.loadInputFiles()
		self.loadOutputFile()
		self.addHistogram3D("XYZ_Position", "Position of CCQE interaction in FGDs", 100, -850, 850, 100, -800, 900, 100, 100, 2000)#Histogram of CCQE neutrino interaction location
		self.addHistogram1D("Neutrino_Momentum", "Momentum of the interacting neutrino(GeV/c)",100,0,5000)#Histogram of interacting neutrino momentum
		self.addHistogram1D("Neutrino_Angle", "Angle of neutrino momentum relative to z axis of ND280 (degrees)",100,0,5)#Histogram of interacting neutrino momentum
		self.addHistogram1D("TPC_Momentum", "Reconstructed momenta of charged particles passing through TPCs from CCQE FGD interactions(GeV/c)",100,0,5000)
		
		self.addHistogramStack("Momentum_PDG","Reconstructed momenta from PIDs and the constituent true particles")
		self.addHistogram1D("Muon_Momentum", "",100,0,5000)
		self.addHistogram1D("Anti_Muon_Momentum", "",100,0,5000)#!! I think some go out of this range, have a look!
		self.addHistogram1D("Proton_Momentum", "",100,0,5000)
		
		self.addHistogramStack("Muon_Pull_PDG","Muon pull from truth particles")
		self.addHistogram1D("Muon_Muon_Pull", "",100,-100,100)
		self.addHistogram1D("Anti_Muon_Muon_Pull", "",100,-100,100)
		self.addHistogram1D("Proton_Muon_Pull", "",100,-100,100)
		
		self.addHistogramStack("Proton_Pull_PDG","Muon pull from truth particles")
		self.addHistogram1D("Muon_Proton_Pull", "",100,-100,100)
		self.addHistogram1D("Anti_Muon_Proton_Pull", "",100,-100,100)
		self.addHistogram1D("Proton_Proton_Pull", "",100,-100,100)
	
	def addHistogram1D(self, name, title, n_bins, minimum, maximum):
		""" Add a 1D histogram to the histogram list """
		self.histograms[ name ] = ROOT.TH1F(name, title, n_bins, minimum, maximum)
	
	
	def addHistogram2D(self, name, title, n_bins_x, minimum_x, maximum_x, n_bins_y, minimum_y, maximum_y):
		""" Add a 1D histogram to the histogram list """
		self.histograms[ name ] = ROOT.TH2F(name, title, n_bins_x, minimum_x, maximum_x, n_bins_y, minimum_y, maximum_y)
		
	def addHistogram3D(self, name, title, n_bins_x, minimum_x, maximum_x, n_bins_y, minimum_y, maximum_y, n_bins_z, minimum_z, maximum_z):
		""" Add a 1D histogram to the histogram list """
		self.histograms[ name ] = ROOT.TH3F(name, title, n_bins_x, minimum_x, maximum_x, n_bins_y, minimum_y, maximum_y, n_bins_z, minimum_z, maximum_z)
		
	def addHistogramStack(self, name, title):
		""" Add a 1D histogram to the histogram list """
		self.histograms[ name ] = ROOT.THStack(name, title)
	
	
	def afterLoop(self):
			
		self.histograms["Muon_Momentum"].SetFillColor(2)
		self.histograms["Momentum_PDG"].Add(self.histograms["Muon_Momentum"])
		self.histograms["Anti_Muon_Momentum"].SetFillColor(3)
		self.histograms["Momentum_PDG"].Add(self.histograms["Anti_Muon_Momentum"])
		self.histograms["Proton_Momentum"].SetFillColor(4)
		self.histograms["Momentum_PDG"].Add(self.histograms["Proton_Momentum"])
		
		self.histograms["Muon_Muon_Pull"].SetFillColor(2)
		self.histograms["Muon_Pull_PDG"].Add(self.histograms["Muon_Muon_Pull"])
		self.histograms["Anti_Muon_Muon_Pull"].SetFillColor(3)
		self.histograms["Muon_Pull_PDG"].Add(self.histograms["Anti_Muon_Muon_Pull"])
		self.histograms["Proton_Muon_Pull"].SetFillColor(4)
		self.histograms["Muon_Pull_PDG"].Add(self.histograms["Proton_Muon_Pull"])
		
		self.histograms["Muon_Proton_Pull"].SetFillColor(2)
		self.histograms["Proton_Pull_PDG"].Add(self.histograms["Muon_Proton_Pull"])
		self.histograms["Anti_Muon_Proton_Pull"].SetFillColor(3)
		self.histograms["Proton_Pull_PDG"].Add(self.histograms["Anti_Muon_Proton_Pull"])
		self.histograms["Proton_Proton_Pull"].SetFillColor(4)
		self.histograms["Proton_Pull_PDG"].Add(self.histograms["Proton_Proton_Pull"])
		
		"""Saves histograms to the output file and prints out any summary information"""
		self.output_file.cd()
		for histogram in self.histograms.itervalues():
			histogram.Write()
		print "Proportion of totel interactions occuring in the FGD:" , float(self.FGDProportion)/float(self.TotalVertices)
		print "Proportion of FGD events that are neutral current:" , float(self.FGDNC)/float(self.FGDProportion)
		print "Proportion of FGD events that are neutral current interacting of neutrons:" , float(self.NCNeutron)/float(self.FGDProportion)
		print "Proportion of CCQE FGD events that have a reconstructed PID:" , float(self.CCQEFGDandPID)/float(self.CCQEFGD)
		print "Proportion of PID reconstructions that are of protons:" , float(self.PIDProton)/float(self.PIDcount)
	
	
	def loadInputFiles(self):
		"""Adds each file in the list of input file names to each module we want to use"""
		for filename in self.input_filename_list:
			for module in self.modules:
				module.Add(filename)
	
	
	def loadModule(self, module_name):
		"""Load all the appropriate modules from the oaAnalysis file that we have defined"""
		module = ROOT.TChain(module_name)
		self.modules.append(module)
		return module
	
	
	def loadOutputFile(self):
		self.output_file = ROOT.TFile(self.output_filename, "RECREATE")
	
	
	def run(self, n = 999999999):
		"""What the user should call when they're ready to run"""
		self.beforeLoop()
		self.runLoop(n)
		self.afterLoop()
	
	
	def runLoop(self, n):
		"""Loops through every event in the files and calls runEvent for each one"""
		
		n = min(n, self.basic_header.GetEntries())
		print "Reading", n, "events"
		
		for i in range(n):
			for module in self.modules:
				module.GetEntry(i)
			self.runEvent()
	
	
	def runEvent(self):
		"""Called for every event in the files"""
 				
		NVtx=self.TruthDir_Vertices.NVtx

		for ivtx in xrange(NVtx):
			vtx=self.TruthDir_Vertices.Vertices[ivtx]
			
			EvtCode=vtx.ReactionCode

			EvtCodeSplitList=EvtCode.split(";")
			
			IncomingPDG=EvtCodeSplitList[0][3:]
						
			TargetNucleus=EvtCodeSplitList[1][4:]		

			if(EvtCodeSplitList[2][:2]=="N:"):
				TargetNucleon=EvtCodeSplitList[2][2:]
				
				if(EvtCodeSplitList[3][:2]=="q:"):
					Current=EvtCodeSplitList[4][10:12]
					InteractionType=EvtCodeSplitList[4].split(",")[1]#could just say coherent?
				else:
					Current=EvtCodeSplitList[3][10:12]
					InteractionType=EvtCodeSplitList[3].split(",")[1]				
					
				
			else:#For coherent scattering
				TargetNucleon=None
				
				Current=EvtCodeSplitList[2][10:12]
				InteractionType=EvtCodeSplitList[2].split(",")[1]
			
			Position=vtx.Position
			
			inFGDX=(Position.X()>=-832.2 and Position.X()<=832.2)
			inFGDY=(Position.Y()>=-777.2 and Position.Y()<=887.2)
			inFGDZ=(Position.Z()>=123.45 and Position.Z()<=446.95) or (Position.Z()>=1481.45 and Position.Z()<=1807.95)

			inFGD=(inFGDX and inFGDY and inFGDZ)

			if(inFGD and Current=="CC" and InteractionType=="QES"):#Checks if in FGD and CCQE interaction
			
				self.histograms["XYZ_Position"].Fill(vtx.Position[0],vtx.Position[1],vtx.Position[2])
				
				Momentum=vtx.NeutrinoMomentum			
				MomentumScalar=math.sqrt(Momentum.X()*Momentum.X()+Momentum.Y()*Momentum.Y()+Momentum.Z()*Momentum.Z())				
				self.histograms["Neutrino_Momentum"].Fill(MomentumScalar)
				
				MomentumXYPlane=math.sqrt(Momentum.X()*Momentum.X()+Momentum.Y()*Momentum.Y())
				
				TanTheta=MomentumXYPlane/Momentum.Z()
				
				Theta=math.atan(TanTheta)*180/math.pi
				
				self.histograms["Neutrino_Angle"].Fill(Theta)
				
				self.CCQEFGD+=1
				
				#Recon: Fraction of CCQEs in FGD with PID
				npids=self.ReconDir_Global.NPIDs
				
				if(npids>0):
					self.CCQEFGDandPID+=1
					
				for i in xrange(npids):
					pid=self.ReconDir_Global.PIDs[i]
					
					pidString=str(pid.Detectors)
					
					TPC1=pidString.find("1")
					TPC2=pidString.find("2")
					TPC3=pidString.find("3")
					
					if(TPC1>-1 or TPC2>-1 or TPC3>-1):
						self.histograms["TPC_Momentum"].Fill(pid.FrontMomentum)
						
					self.PIDcount+=1
					
					Particle=pid.TrueParticle
					
					TrajectoryID=Particle.ID
					
					NTrajectory=self.TruthDir_Trajectories.NTraj
					
					for traj in xrange(NTrajectory):#loops over all trajectories in an event
						Trajectory=self.TruthDir_Trajectories.Trajectories[traj]
						
						if(Trajectory.ID==TrajectoryID):#if: the trajectory ID in the loop matches that of the recon pid
							if(Trajectory.PDG==2212):#checks if proton
								self.PIDProton+=1
								
					#Exercise 3:
					
					for traj in xrange(NTrajectory):#loops over all trajectories in an event
						Trajectory=self.TruthDir_Trajectories.Trajectories[traj]
						
						if(Trajectory.ID==TrajectoryID):#if: the trajectory ID in the loop matches that of the recon pid
							TruePDG=Trajectory.PDG
							
					if(TruePDG==13):
						self.histograms["Muon_Momentum"].Fill(pid.FrontMomentum)
					elif(TruePDG==-13):
						self.histograms["Anti_Muon_Momentum"].Fill(pid.FrontMomentum)
					elif(TruePDG==2212):
						self.histograms["Proton_Momentum"].Fill(pid.FrontMomentum)

					#Muon Pull
						
					NumberTPC=pid.NTPCs
					
					for tpccounter in xrange(NumberTPC):
						TpcTrack=pid.TPC[tpccounter]
						
						if(TruePDG==13):
							self.histograms["Muon_Muon_Pull"].Fill(TpcTrack.PullMuon)
							self.histograms["Muon_Proton_Pull"].Fill(TpcTrack.PullProton)
						elif(TruePDG==-13):
							self.histograms["Anti_Muon_Muon_Pull"].Fill(TpcTrack.PullMuon)
							self.histograms["Anti_Muon_Proton_Pull"].Fill(TpcTrack.PullProton)
						elif(TruePDG==2212):
							self.histograms["Proton_Muon_Pull"].Fill(TpcTrack.PullMuon)
							self.histograms["Proton_Proton_Pull"].Fill(TpcTrack.PullProton)
					
			if(inFGD):
				self.FGDProportion+=1
				
			if(inFGD and Current=="NC"):
				self.FGDNC+=1
				
			if(inFGD and Current=="NC" and TargetNucleon==2112):
				self.NCNeutron+=1

			self.TotalVertices+=1

			

		
def main():
	
	if( len(sys.argv) != 3 ):
		print "[USAGE]: python example_analysis.py path/to/files/input_file_pattern output_filename.root"
		return
	
	# Always load the libraries, or nothing will work
	# Make sure the libraries were made with the same version of ROOT as the analysis files were produced with
	libraries.load("nd280/nd280.so")
	
	# glob returns a list of all files mathing the expression given to it
	#input_filename_list = ( glob.glob( sys.argv[1]+"*" ) )
	
	FileList = open("prod5_analysis.list")
	
	input_filename_list = FileList.read().splitlines()
	
	output_filename = sys.argv[2]
	
	analysis = Analysis(input_filename_list, output_filename)
	analysis.run(10000)

	

if __name__ == "__main__":
	main()
