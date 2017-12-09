//////////////////////////////////////////////////////////
//   This class has been generated by TFile::MakeProject
//     (Wed Nov 21 16:59:09 2012 by ROOT version 5.32/00)
//      from the StreamerInfo in file /storage/epp2/phseaj/exercise/prod5_analysis.root
//////////////////////////////////////////////////////////


#ifndef ND__TTruthTrajectoriesModule_h
#define ND__TTruthTrajectoriesModule_h
namespace ND {
class TTruthTrajectoriesModule;
} // end of namespace.

#include "ND__TAnalysisTruthModuleBase.h"
#include "Riostream.h"
#include <set>
#include "TClonesArray.h"
#include "TObject.h"
#include <string>
#include "TLorentzVector.h"
#include <vector>
#include "TVector3.h"

namespace ND {
class TTruthTrajectoriesModule : public ND::TAnalysisTruthModuleBase {

public:
// Nested classes forward declaration.
class TTruthTrajectory;

public:
// Nested classes declaration.
class TTruthTrajectory : public TObject {

public:
// Nested classes declaration.

public:
// Data Members.
   Int_t       ID;          //
   Int_t       PDG;         //
   string      Name;        //
   Int_t       Category;    //
   TLorentzVector InitMomentum;    //
   TLorentzVector InitPosition;    //
   TLorentzVector FinalPosition;    //
   Int_t          ParentID;         //
   Int_t          PrimaryID;        //
   double         Mass;             //
   int            Charge;           //
   vector<int>    TraceSubdetectors;    //
   vector<bool>   TraceInActive;        //
   vector<TLorentzVector> TraceEntrancePosition;    //
   vector<TLorentzVector> TraceExitPosition;        //
   vector<TVector3>       TraceEntranceMomentum;    //
   vector<TVector3>       TraceExitMomentum;        //
   Int_t                  InitSubdetector;          //
   Int_t                  FinalSubdetector;         //
   Bool_t                 EnteredSubdetector[13];    //
   Bool_t                 ExitedSubdetector[13];     //
   TLorentzVector         EntrancePosition[13];      //
   TLorentzVector         ExitPosition[13];          //
   TVector3               EntranceMomentum[13];      //
   TVector3               ExitMomentum[13];          //

   TTruthTrajectory();
   TTruthTrajectory(const TTruthTrajectory & );
   virtual ~TTruthTrajectory();

   ClassDef(TTruthTrajectory,2); // Generated by MakeProject.
};

public:
// Data Members.
   UInt_t      fMaxNTrajectories;    //
   Double_t    fMinLength;           //
   Bool_t      fSaveOnlyP0DTrackerECALTrajectories;    //
   Bool_t      fSaveParentChain;                       //
   std::set<int> fSaveList;                              //
   Int_t         fNTraj;                                 //
   Int_t         fNTrajLepton;                           //
   Int_t         fNTrajBaryon;                           //
   Int_t         fNTrajMeson;                            //
   Int_t         fNTrajPhoton;                           //
   Int_t         fNTrajOtherCharged;                     //
   Int_t         fNTrajOtherNeutral;                     //
   Int_t         fNTrajOther;                            //
   TClonesArray* fTrajectories;                          //

   TTruthTrajectoriesModule();
   TTruthTrajectoriesModule(const TTruthTrajectoriesModule & );
   virtual ~TTruthTrajectoriesModule();

   ClassDef(TTruthTrajectoriesModule,2); // Generated by MakeProject.
};
} // namespace
#endif
