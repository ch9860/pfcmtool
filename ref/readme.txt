vic.ho@Vic-Ho MINGW64 /c/proj/src/pfcm/bhs
$ find ./ -name .git
./BaseTools/.git
./Board/Intel/BirchStreamMultiBoardPkg/.git
./EDK2/.git
./Insyde/.git
./Insyde/InsydeModulePkg/Bus/Pci/AhciBusDxe/.git
./Insyde/InsydeModulePkg/Bus/Pci/AhciBusPei/.git
./Insyde/InsydeModulePkg/Bus/Pci/EhciDxe/.git
./Insyde/InsydeModulePkg/Bus/Pci/EhciPei/.git
./Insyde/InsydeModulePkg/Bus/Pci/NvmExpressDxe/.git
./Insyde/InsydeModulePkg/Bus/Pci/NvmExpressPei/.git
./Insyde/InsydeModulePkg/Bus/Pci/SdhcDxe/.git
./Insyde/InsydeModulePkg/Bus/Pci/SdhcPei/.git
./Insyde/InsydeModulePkg/Bus/Pci/UfsDxe/.git
./Insyde/InsydeModulePkg/Bus/Pci/UfsPei/.git
./Insyde/InsydeModulePkg/Bus/Pci/XhciDxe/.git
./Insyde/InsydeModulePkg/Bus/Pci/XhciPei/.git
./Insyde/InsydeModulePkg/Csm/.git
./Insyde/InsydeModulePkg/H2ODebug/.git
./Insyde/InsydeSamplePkg/.git
./Insyde/SioDummyPkg/.git
./Intel/BirchStream/.git
./Intel/EDK2Platforms/.git
./SegFeature/InsydeAdvBootPkg/.git
./SegFeature/InsydeCrPkg/.git
./SegFeature/InsydeH2OUvePkg/.git
./SegFeature/InsydeIpmiPkg/.git
./SegFeature/SegFeaturePkg/.git
./Sio/SioAst2xxxPkg/.git

vic.ho@Vic-Ho MINGW64 /c/proj/src/pfcm/bhs
$ find ./ -name *.pfc
./Board/Intel/BirchStreamMultiBoardPkg/Project.pfc

vic.ho@Vic-Ho MINGW64 /c/proj/src/pfcm/bhs
$ find ./ -name *.ifc
./BaseTools/Kernel_BaseToolsBin_Rev5.6.ifc
./Board/Intel/BirchStreamMultiBoardPkg/Intel_BirchStream_MultiBoard_Rev5.6.ifc
./EDK2/Intel_BirchStreamEDK2.ifc
./Insyde/InsydeModulePkg/Bus/Pci/AhciBusDxe/Kernel_AhciBusDxeBin_Rev5.6.ifc
./Insyde/InsydeModulePkg/Bus/Pci/AhciBusPei/Kernel_AhciBusPeiBin_Rev5.6.ifc
./Insyde/InsydeModulePkg/Bus/Pci/EhciDxe/Kernel_EhciDxeBin_Rev5.6.ifc
./Insyde/InsydeModulePkg/Bus/Pci/EhciPei/Kernel_EhciPeiBin_Rev5.6.ifc
./Insyde/InsydeModulePkg/Bus/Pci/NvmExpressDxe/Kernel_NvmExpressDxeBin_Rev5.6.ifc
./Insyde/InsydeModulePkg/Bus/Pci/NvmExpressPei/Kernel_NvmExpressPeiBin_Rev5.6.ifc
./Insyde/InsydeModulePkg/Bus/Pci/SdhcDxe/Kernel_SdhcDxeBin_Rev5.6.ifc
./Insyde/InsydeModulePkg/Bus/Pci/SdhcPei/Kernel_SdhcPeiBin_Rev5.6.ifc
./Insyde/InsydeModulePkg/Bus/Pci/UfsDxe/Kernel_UfsDxeBin_Rev5.6.ifc
./Insyde/InsydeModulePkg/Bus/Pci/UfsPei/Kernel_UfsPeiBin_Rev5.6.ifc
./Insyde/InsydeModulePkg/Bus/Pci/XhciDxe/Kernel_XhciDxeBin_Rev5.6.ifc
./Insyde/InsydeModulePkg/Bus/Pci/XhciPei/Kernel_XhciPeiBin_Rev5.6.ifc
./Insyde/InsydeModulePkg/Csm/Kernel_Csm_Rev5.6.ifc
./Insyde/InsydeModulePkg/H2ODebug/Kernel_H2ODebug_Rev5.6.ifc
./Insyde/InsydeSamplePkg/Kernel_InsydeSamplePkg_Rev5.6.ifc
./Insyde/Kernel_Base_Rev5.6.ifc
./Insyde/SioDummyPkg/Kernel_SioDummyPkg_Rev5.6.ifc
./Intel/BirchStream/Intel_BirchStream.ifc
./Intel/EDK2Platforms/Intel_EDK2Platforms.ifc
./SegFeature/InsydeAdvBootPkg/InsydeAdvBootPkg.ifc
./SegFeature/InsydeCrPkg/InsydeCrPkg.ifc
./SegFeature/InsydeH2OUvePkg/InsydeH2OUvePkg.ifc
./SegFeature/InsydeIpmiPkg/InsydeIpmiPkg.ifc
./SegFeature/SegFeaturePkg/InsydeSegFeaturePkg.ifc
./Sio/SioAst2xxxPkg/Aspeed_Ast2xxx.ifc


cd BaseTools/
echo "BaseTools/Kernel_BaseToolsBin_Rev5.6"
echo "BaseTools/Kernel_BaseToolsBin_Rev5.6" 2>&1 > ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Board/Intel/BirchStreamMultiBoardPkg/
echo "Board/Intel/BirchStreamMultiBoardPkg/Intel_BirchStream_MultiBoard_Rev5.6"
echo "Board/Intel/BirchStreamMultiBoardPkg/Intel_BirchStream_MultiBoard_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd EDK2/
echo "EDK2/Intel_BirchStreamEDK2"
echo "EDK2/Intel_BirchStreamEDK2" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Insyde/InsydeModulePkg/Bus/Pci/AhciBusDxe/
echo "Insyde/InsydeModulePkg/Bus/Pci/AhciBusDxe/Kernel_AhciBusDxeBin_Rev5.6"
echo "Insyde/InsydeModulePkg/Bus/Pci/AhciBusDxe/Kernel_AhciBusDxeBin_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Insyde/InsydeModulePkg/Bus/Pci/AhciBusPei/
echo "Insyde/InsydeModulePkg/Bus/Pci/AhciBusPei/Kernel_AhciBusPeiBin_Rev5.6"
echo "Insyde/InsydeModulePkg/Bus/Pci/AhciBusPei/Kernel_AhciBusPeiBin_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Insyde/InsydeModulePkg/Bus/Pci/EhciDxe/
echo "Insyde/InsydeModulePkg/Bus/Pci/EhciDxe/Kernel_EhciDxeBin_Rev5.6"
echo "Insyde/InsydeModulePkg/Bus/Pci/EhciDxe/Kernel_EhciDxeBin_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Insyde/InsydeModulePkg/Bus/Pci/EhciPei/
echo "Insyde/InsydeModulePkg/Bus/Pci/EhciPei/Kernel_EhciPeiBin_Rev5.6"
echo "Insyde/InsydeModulePkg/Bus/Pci/EhciPei/Kernel_EhciPeiBin_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Insyde/InsydeModulePkg/Bus/Pci/NvmExpressDxe/
echo "Insyde/InsydeModulePkg/Bus/Pci/NvmExpressDxe/Kernel_NvmExpressDxeBin_Rev5.6"
echo "Insyde/InsydeModulePkg/Bus/Pci/NvmExpressDxe/Kernel_NvmExpressDxeBin_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Insyde/InsydeModulePkg/Bus/Pci/NvmExpressPei/
echo "Insyde/InsydeModulePkg/Bus/Pci/NvmExpressPei/Kernel_NvmExpressPeiBin_Rev5.6"
echo "Insyde/InsydeModulePkg/Bus/Pci/NvmExpressPei/Kernel_NvmExpressPeiBin_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Insyde/InsydeModulePkg/Bus/Pci/SdhcDxe/
echo "Insyde/InsydeModulePkg/Bus/Pci/SdhcDxe/Kernel_SdhcDxeBin_Rev5.6"
echo "Insyde/InsydeModulePkg/Bus/Pci/SdhcDxe/Kernel_SdhcDxeBin_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Insyde/InsydeModulePkg/Bus/Pci/SdhcPei/
echo "Insyde/InsydeModulePkg/Bus/Pci/SdhcPei/Kernel_SdhcPeiBin_Rev5.6"
echo "Insyde/InsydeModulePkg/Bus/Pci/SdhcPei/Kernel_SdhcPeiBin_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Insyde/InsydeModulePkg/Bus/Pci/UfsDxe/
echo "Insyde/InsydeModulePkg/Bus/Pci/UfsDxe/Kernel_UfsDxeBin_Rev5.6"
echo "Insyde/InsydeModulePkg/Bus/Pci/UfsDxe/Kernel_UfsDxeBin_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Insyde/InsydeModulePkg/Bus/Pci/UfsPei/
echo "Insyde/InsydeModulePkg/Bus/Pci/UfsPei/Kernel_UfsPeiBin_Rev5.6"
echo "Insyde/InsydeModulePkg/Bus/Pci/UfsPei/Kernel_UfsPeiBin_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Insyde/InsydeModulePkg/Bus/Pci/XhciDxe/
echo "Insyde/InsydeModulePkg/Bus/Pci/XhciDxe/Kernel_XhciDxeBin_Rev5.6"
echo "Insyde/InsydeModulePkg/Bus/Pci/XhciDxe/Kernel_XhciDxeBin_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Insyde/InsydeModulePkg/Bus/Pci/XhciPei/
echo "Insyde/InsydeModulePkg/Bus/Pci/XhciPei/Kernel_XhciPeiBin_Rev5.6"
echo "Insyde/InsydeModulePkg/Bus/Pci/XhciPei/Kernel_XhciPeiBin_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Insyde/InsydeModulePkg/Csm/
echo "Insyde/InsydeModulePkg/Csm/Kernel_Csm_Rev5.6"
echo "Insyde/InsydeModulePkg/Csm/Kernel_Csm_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Insyde/InsydeModulePkg/H2ODebug/
echo "Insyde/InsydeModulePkg/H2ODebug/Kernel_H2ODebug_Rev5.6"
echo "Insyde/InsydeModulePkg/H2ODebug/Kernel_H2ODebug_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Insyde/InsydeSamplePkg/
echo "Insyde/InsydeSamplePkg/Kernel_InsydeSamplePkg_Rev5.6"
echo "Insyde/InsydeSamplePkg/Kernel_InsydeSamplePkg_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Insyde/
echo "Insyde/Kernel_Base_Rev5.6"
echo "Insyde/Kernel_Base_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Insyde/SioDummyPkg/
echo "Insyde/SioDummyPkg/Kernel_SioDummyPkg_Rev5.6"
echo "Insyde/SioDummyPkg/Kernel_SioDummyPkg_Rev5.6" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Intel/BirchStream/
echo "Intel/BirchStream/Intel_BirchStream"
echo "Intel/BirchStream/Intel_BirchStream" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Intel/EDK2Platforms/
echo "Intel/EDK2Platforms/Intel_EDK2Platforms"
echo "Intel/EDK2Platforms/Intel_EDK2Platforms" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd SegFeature/InsydeAdvBootPkg/
echo "SegFeature/InsydeAdvBootPkg/InsydeAdvBootPkg"
echo "SegFeature/InsydeAdvBootPkg/InsydeAdvBootPkg" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd SegFeature/InsydeCrPkg/
echo "SegFeature/InsydeCrPkg/InsydeCrPkg"
echo "SegFeature/InsydeCrPkg/InsydeCrPkg" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd SegFeature/InsydeH2OUvePkg/
echo "SegFeature/InsydeH2OUvePkg/InsydeH2OUvePkg"
echo "SegFeature/InsydeH2OUvePkg/InsydeH2OUvePkg" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd SegFeature/InsydeIpmiPkg/
echo "SegFeature/InsydeIpmiPkg/InsydeIpmiPkg"
echo "SegFeature/InsydeIpmiPkg/InsydeIpmiPkg" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd SegFeature/SegFeaturePkg/
echo "SegFeature/SegFeaturePkg/InsydeSegFeaturePkg"
echo "SegFeature/SegFeaturePkg/InsydeSegFeaturePkg" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -
cd Sio/SioAst2xxxPkg/
echo "Sio/SioAst2xxxPkg/Aspeed_Ast2xxx"
echo "Sio/SioAst2xxxPkg/Aspeed_Ast2xxx" 2>&1 >> ~/output.txt 
git rev-parse HEAD 2>&1 >> ~/output.txt 
git describe --tags --exact-match >> ~/output.txt
echo "    " >> ~/output.txt
cd -




