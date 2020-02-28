#ifdef __CLING__
R__LOAD_LIBRARY(libDelphes.so)
#include "classes/DelphesClasses.h"
#include "external/ExRootAnalysis/ExRootTreeReader.h"
#include <iostream>
#include <fstream>	
#endif




void SelectDark3(const char *inputFile, const char *outputFile, const char *logout) {
// Example of Root macro to copy a subset of a Tree to a new Tree
// Only selected entries are copied to the new Tree.

   //gSystem->Load("$ROOTSYS/test/libEvent");
   //gSystem->Load("libEvent");
   //gSystem->Load("libDelphes");
   
   //Get old file, old tree and set top branch address
   TChain chain("Delphes");
   chain.Add(inputFile);
   ExRootTreeReader *viejotree = new ExRootTreeReader(&chain);
   TClonesArray *branchMuon = viejotree->UseBranch("Muon");

   TFile *oldfile = new TFile(inputFile);
   TTree *oldtree = (TTree*)oldfile->Get("Delphes;1");
   Long64_t nentries = oldtree->GetEntries();
   Int_t event   = 0;

   //branchMuon = oldtree->Branch("Muon");
   
//Event *event   = 0;
   //oldtree->SetBranchAddress("event",&event);

   //Create a new file + a clone of old tree in new file
   TFile *newfile = new TFile(outputFile,"recreate");
   TTree *newtree = oldtree->CloneTree(0);
    
   // file
   ofstream file;
   file.open(logout);
  



   file << "Eventos incluidos\n";
   for (Long64_t i=0;i<nentries; i++) {
      oldtree->GetEntry(i);
      viejotree->ReadEntry(i);
      if (branchMuon->GetEntries() > 3) newtree->Fill(), file << i << "\n";//i < 5000

      //event->Clear();
   }
   //newtree->Print();
   newtree->AutoSave();
   delete oldfile;
   delete newfile;
   file.close();
}
