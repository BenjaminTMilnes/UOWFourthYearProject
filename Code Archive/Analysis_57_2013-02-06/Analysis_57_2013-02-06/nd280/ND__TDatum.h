//////////////////////////////////////////////////////////
//   This class has been generated by TFile::MakeProject
//     (Sun Dec 23 15:43:19 2012 by ROOT version 5.32/00)
//      from the StreamerInfo in file /storage/epp2/phseaj/exercise/prod5_analysis.root
//////////////////////////////////////////////////////////


#ifndef ND__TDatum_h
#define ND__TDatum_h
namespace ND {
class TDatum;
} // end of namespace.

#include "TNamed.h"
#include "ND__TDatum.h"

namespace ND {
class TDatum : public TNamed {

public:
// Nested classes declaration.

public:
// Data Members.
   ND::TDatum* fParent;     //

   TDatum();
   TDatum(const TDatum & );
   virtual ~TDatum();

   ClassDef(TDatum,3); // Generated by MakeProject.
};
} // namespace
#endif
