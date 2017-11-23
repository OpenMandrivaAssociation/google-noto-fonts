#!/bin/sh
pkg_name="google-noto-fonts"

for a in *.zip; do
	mkdir -p $pkg_name
	unzip -o -d $pkg_name $a
done

rm $pkg_name/LICENSE*.txt $pkg_name/README
# remove draft fonts for now
#rm -f $pkg_name/*Draft.*tf

cp -f $pkg_name.spec.in $pkg_name.spec
for h in hinted; do
	ls $pkg_name/ | sed -e 's:Noto::' -e 's:-.*\..tf::' -e 's:\..tf::' -e 's:\.ttc::' | sort | uniq | while read font; do 
		serif=""
		for i in SansMono Mono Sans Serif; do
			if echo $font |grep -q $i; then
				serif=$i
				break
			fi
		done
		ui="`(echo $font | grep -q UI) && echo -n UI`"
		script=`echo $font | sed "s:$serif\(.*\)$ui:\1:"`
		if echo $script |grep -qE '^CJK'; then
			if echo " $HAVE_CJK " |grep -q " $serif "; then
				continue
			fi
			script="CJK"
			HAVE_CJK="$HAVE_CJK $serif"
		fi
		packagename="noto"
		if [ -n "$serif" ]; then
			if [ "$serif" = "SansMono" ]; then
				packagename="$packagename-sans-mono"
			else
				packagename="$packagename-$serif"
			fi
		fi
		[ -n "$script" ] && packagename="$packagename-$script"
		[ -n "$ui" ] && packagename="$packagename-$ui"
		packagename=`echo "$packagename" | tr 'A-Z' 'a-z'`
		if [ "$serif" == "SansMono" ]; then
			serif_dsc="Monospace Sans Serif"
		elif [ "$serif" == "Sans" ]; then
			serif_dsc="Sans Serif"
		else
			serif_dsc="$serif"
		fi
		obsoletes=$packagename
		if [ "$script" == "CJK" ]; then
			if [ "$serif" == "SansMono" ]; then
				obserif="sans-mono"
			else
				obserif=`echo $serif |tr A-Z a-z`
			fi
			for l in jp kr sc tc ; do
				obsoletes="$obsoletes noto-$obserif-cjk$l noto-$obserif-cjk$l-fonts "
			done
			for j in zh-CN zh-SG zh-TW zh-HK zh-MO ja ko ; do
				scalables="$scalables scalable-font-$j"
			done
		fi
		packagename="$packagename-fonts"
		summary=`echo "Noto $script $serif_dsc Font" | sed 's:\([a-z]\)\([A-Z]\):\1 \2:;s:  +: :g'`

		sed -i "s/@SUBPACKAGE_HEADERS@/%package -n $packagename\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
		sed -i "s/@SUBPACKAGE_HEADERS@/Summary:	$summary\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
		sed -i "s;@SUBPACKAGE_HEADERS@;Group:		System/Fonts/True type\n@SUBPACKAGE_HEADERS@;" $pkg_name.spec
		sed -i "s/@SUBPACKAGE_HEADERS@/Suggests:	$pkg_name-doc\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
		for i in $obsoletes ; do
			sed -i "s/@SUBPACKAGE_HEADERS@/Obsoletes:	$i\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
			sed -i "s/@SUBPACKAGE_HEADERS@/Provides:	$i\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
		done
		if [ "$script" == "CJK" ]; then
			for i in $scalables ; do
				sed -i "s/@SUBPACKAGE_HEADERS@/Provides:	$i\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
			done
			sed -i "s/@SUBPACKAGE_HEADERS@/Provides:	locale(zh_CN;zh_SG;zh_TW;zh_HK;zh_MO)\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
		fi
		sed -i "s/@SUBPACKAGE_HEADERS@/\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
		sed -i "s/@SUBPACKAGE_HEADERS@/%description -n $packagename\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
		sed -i "s/@SUBPACKAGE_HEADERS@/Noto's design goal is to achieve visual harmonization (e.g., compatible\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
		sed -i "s/@SUBPACKAGE_HEADERS@/heights and stroke thicknesses) across languages. This package contains\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
		sed -i "s/@SUBPACKAGE_HEADERS@/$script $serif_dsc font, $h.\n@SUBPACKAGE_HEADERS@/;s,^ +,,;s,  *, ,g" $pkg_name.spec
		sed -i "s/@SUBPACKAGE_HEADERS@/\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec

		sed -i "s/@SUBPACKAGE_FILELISTS@/%files -n $packagename\n@SUBPACKAGE_FILELISTS@/" $pkg_name.spec
		sed -i "s/@SUBPACKAGE_FILELISTS@/%dir %{_ttfontsdir}\n@SUBPACKAGE_FILELISTS@/" $pkg_name.spec
		if [ "$script" == "ColorEmoji" ]; then
			sed -i "s:@SUBPACKAGE_FILELISTS@:%{_ttfontsdir}/Noto$serif$script$ui\*.?tf\n@SUBPACKAGE_FILELISTS@:" $pkg_name.spec
		elif [ "$script" == "CJK" ]; then
			sed -i "s:@SUBPACKAGE_FILELISTS@:%{_ttfontsdir}/Noto$serif$script$ui\*.*\n@SUBPACKAGE_FILELISTS@:" $pkg_name.spec
			if [ "$serif" = "Sans" ]; then
				sed -i "s:@SUBPACKAGE_FILELISTS@:%{_fontconfig_templatedir}/59*.conf\n@SUBPACKAGE_FILELISTS@:" $pkg_name.spec
				sed -i "s:@SUBPACKAGE_FILELISTS@:%config(noreplace) %{_fontconfig_confdir}/59*.conf\n@SUBPACKAGE_FILELISTS@:" $pkg_name.spec
			fi
		else
			sed -i "s:@SUBPACKAGE_FILELISTS@:%{_ttfontsdir}/Noto$serif$script$ui-\*.?tf\n@SUBPACKAGE_FILELISTS@:" $pkg_name.spec
		fi
		sed -i "s/@SUBPACKAGE_FILELISTS@/\n@SUBPACKAGE_FILELISTS@/" $pkg_name.spec
	done
done

sed -i 's/@SUBPACKAGE_HEADERS@//' $pkg_name.spec
sed -i 's/@SUBPACKAGE_SCRIPTLETS@//' $pkg_name.spec
sed -i 's/@SUBPACKAGE_FILELISTS@//' $pkg_name.spec

rm -r $pkg_name
