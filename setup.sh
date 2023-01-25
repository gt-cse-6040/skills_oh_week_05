if [ -d "resource" ]; then
  rm -r resource
fi

if [ -d "tester_fw" ]; then
  rm -r tester_fw
fi

mkdir tester_fw
mkdir -p resource/asnlib/publicdata/encrypted
mkdir resource/asnlib/public
wget -q https://raw.githubusercontent.com/gt-cse-6040/skills_oh_week_05/main/public.txt
wget -q https://raw.githubusercontent.com/gt-cse-6040/skills_oh_week_05/main/publicdata.txt
wget -q https://raw.githubusercontent.com/gt-cse-6040/skills_oh_week_05/main/publicdata_encrypted.txt
wget -q https://raw.githubusercontent.com/gt-cse-6040/skills_oh_week_05/main/tester_fw.txt
wget -P tester_fw/ -i tester_fw.txt -q
wget -P resource/asnlib/public/ -i public.txt -q
wget -P resource/asnlib/publicdata/ -i publicdata.txt -q
wget -P resource/asnlib/publicdata/encrypted -i publicdata_encrypted.txt -q
pip install cryptography
rm public.txt publicdata.txt publicdata_encrypted.txt tester_fw.txt
