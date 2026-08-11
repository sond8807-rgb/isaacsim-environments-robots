# Importing an IFC2X3 file to Isaac Sim (v5.1.0)

1. Enable the CAD Converter extension in Isaac Sim: Window \> Extensions \> CAD Converter.  
2. Import the IFC file:  File \> Import, then select the .ifc file. Make sure to check “Convert Metadata”:  
<img width="1350" height="875" alt="Screenshot from 2026-08-11 11-28-01" src="https://github.com/user-attachments/assets/cdae2b43-52f7-4970-8c89-2344b94df6f6" />

3. The building should now appear in the simulation. It should look something like this:  
<img width="3509" height="985" alt="Screenshot from 2026-08-11 11-30-45" src="https://github.com/user-attachments/assets/21267bc2-f034-47dc-adff-ed430a580181" />

4. I verified the dimensions, metadata and entity numbers and they all matched the IFC source file (see [https://drive.google.com/file/d/1fA31TkD13dPNqLazXU2Bf-ynctsYU9iZ/view?usp=sharing](https://drive.google.com/file/d/1fA31TkD13dPNqLazXU2Bf-ynctsYU9iZ/view?usp=sharing) for verification details). The IFC2X3 to Isaac Sim (v5.1.0) pipeline should therefore work accurately
