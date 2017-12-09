//////////////////////////////////////////////////////////
//   This class has been generated by TFile::MakeProject
//     (Thu Dec  6 16:29:43 2012 by ROOT version 5.32/00)
//      from the StreamerInfo in file /storage/epp2/phseaj/exercise/prod5_analysis.root
//////////////////////////////////////////////////////////


#ifndef ND__TSubBaseObject_h
#define ND__TSubBaseObject_h
namespace ND {
class TSubBaseObject;
} // end of namespace.

#include "TObject.h"
#include "TLorentzVector.h"
#include "TVector3.h"
#include "ND__TTrueParticle.h"

namespace ND {
class TSubBaseObject : public TObject {

public:
// Nested classes declaration.

public:
// Data Members.
   UInt_t      UniqueID;    //
   unsigned long Status;      //
   int           Detector;    //
   int           NHits;       //
   int           NNodes;      //
   int           NDOF;        //
   double        Chi2;        //
   double        EDeposit;    //
   int           NConstituents;    //
   double        Length;           //
   TLorentzVector FrontPosition;    //
   TLorentzVector BackPosition;     //
   TLorentzVector FrontPositionVar;    //
   TLorentzVector BackPositionVar;     //
   TVector3       FrontDirection;      //
   TVector3       BackDirection;       //
   TVector3       FrontDirectionVar;    //
   TVector3       BackDirectionVar;     //
   double         FrontMomentum;        //
   double         BackMomentum;         //
   double         FrontMomentumError;    //
   double         BackMomentumError;     //
   ND::TTrueParticle TrueParticle;          //

   TSubBaseObject();
   TSubBaseObject(const TSubBaseObject & );
   virtual ~TSubBaseObject();

   ClassDef(TSubBaseObject,2); // Generated by MakeProject.
};
} // namespace
#endif
