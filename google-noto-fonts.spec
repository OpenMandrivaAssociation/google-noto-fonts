#
# spec file for package google-noto-fonts
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define hyear     2015
%define hmonth    12
%define hday      15
%define src_name  NotoFonts

%define _ttfontsdir %{_datadir}/fonts/TTF/

# DO NOT EDIT THIS SPECFILE DIRECTLY, edit google-noto-fonts.spec.in and run generate-specfile.sh scriptZZ

Name:           google-noto-fonts
Version:        %{hyear}%{hmonth}%{hday}
Release:        1
Summary:        Noto Font Families
License:        OFL-1.1
Group:          System/Fonts/True type
Url:            https://github.com/googlei18n/noto-fonts
Source0:        https://noto-website-2.storage.googleapis.com/pkgs/Noto-hinted.zip
Source1:        https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJK.ttc.zip
Source2:        generate-specfile.sh
Source3:        59-noto-sans-cjk.conf
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch

%description
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. 

%package doc
Summary:        Noto Font Families License
Group:          System/Fonts/True Type

%description doc
License for Google's Noto fonts.

%package -n noto-coloremoji-fonts
Summary:        Noto   Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-coloremoji
Provides:       noto-coloremoji

%description -n noto-coloremoji-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
  font, hinted.

%package -n noto-emoji-fonts
Summary:        Noto   Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-emoji
Provides:       noto-emoji

%description -n noto-emoji-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
  font, hinted.

%package -n noto-kufiarabic-fonts
Summary:        Noto   Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-kufiarabic
Provides:       noto-kufiarabic

%description -n noto-kufiarabic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
  font, hinted.

%package -n noto-naskharabic-fonts
Summary:        Noto   Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-naskharabic
Provides:       noto-naskharabic

%description -n noto-naskharabic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
  font, hinted.

%package -n noto-nastaliqurdu-fonts
Summary:        Noto   Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-nastaliqurdu
Provides:       noto-nastaliqurdu

%description -n noto-nastaliqurdu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
  font, hinted.

%package -n noto-sans-fonts
Summary:        Noto  Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans
Provides:       noto-sans

%description -n noto-sans-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
 Sans Serif font, hinted.

%package -n noto-sans-armenian-fonts
Summary:        Noto Armenian Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-armenian
Provides:       noto-sans-armenian

%description -n noto-sans-armenian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Armenian Sans Serif font, hinted.

%package -n noto-sans-avestan-fonts
Summary:        Noto Avestan Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-avestan
Provides:       noto-sans-avestan

%description -n noto-sans-avestan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Avestan Sans Serif font, hinted.

%package -n noto-sans-balinese-fonts
Summary:        Noto Balinese Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-balinese
Provides:       noto-sans-balinese

%description -n noto-sans-balinese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Balinese Sans Serif font, hinted.

%package -n noto-sans-bamum-fonts
Summary:        Noto Bamum Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-bamum
Provides:       noto-sans-bamum

%description -n noto-sans-bamum-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bamum Sans Serif font, hinted.

%package -n noto-sans-batak-fonts
Summary:        Noto Batak Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-batak
Provides:       noto-sans-batak

%description -n noto-sans-batak-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Batak Sans Serif font, hinted.

%package -n noto-sans-bengali-fonts
Summary:        Noto Bengali Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-bengali
Provides:       noto-sans-bengali

%description -n noto-sans-bengali-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bengali Sans Serif font, hinted.

%package -n noto-sans-brahmi-fonts
Summary:        Noto Brahmi Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-brahmi
Provides:       noto-sans-brahmi

%description -n noto-sans-brahmi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Brahmi Sans Serif font, hinted.

%package -n noto-sans-buginese-fonts
Summary:        Noto Buginese Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-buginese
Provides:       noto-sans-buginese

%description -n noto-sans-buginese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Buginese Sans Serif font, hinted.

%package -n noto-sans-buhid-fonts
Summary:        Noto Buhid Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-buhid
Provides:       noto-sans-buhid

%description -n noto-sans-buhid-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Buhid Sans Serif font, hinted.

%package -n noto-sans-cjk-fonts
Summary:        Noto CJK Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-cjk
Provides:       noto-sans-cjk
Obsoletes:      noto-sans-cjkjp
Provides:       noto-sans-cjkjp
Obsoletes:      noto-sans-cjkjp-fonts
Provides:       noto-sans-cjkjp-fonts
Obsoletes:      noto-sans-cjkkr
Provides:       noto-sans-cjkkr
Obsoletes:      noto-sans-cjkkr-fonts
Provides:       noto-sans-cjkkr-fonts
Obsoletes:      noto-sans-cjksc
Provides:       noto-sans-cjksc
Obsoletes:      noto-sans-cjksc-fonts
Provides:       noto-sans-cjksc-fonts
Obsoletes:      noto-sans-cjktc
Provides:       noto-sans-cjktc
Obsoletes:      noto-sans-cjktc-fonts
Provides:       noto-sans-cjktc-fonts
Provides:       scalable-font-zh-CN
Provides:       scalable-font-zh-SG
Provides:       scalable-font-zh-TW
Provides:       scalable-font-zh-HK
Provides:       scalable-font-zh-MO
Provides:       scalable-font-ja
Provides:       scalable-font-ko
Provides:       locale(zh_CN;zh_SG;zh_TW;zh_HK;zh_MO)

%description -n noto-sans-cjk-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
CJK Sans Serif font, hinted.

%package -n noto-sans-canadianaboriginal-fonts
Summary:        Noto Canadian Aboriginal Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-canadianaboriginal
Provides:       noto-sans-canadianaboriginal

%description -n noto-sans-canadianaboriginal-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
CanadianAboriginal Sans Serif font, hinted.

%package -n noto-sans-carian-fonts
Summary:        Noto Carian Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-carian
Provides:       noto-sans-carian

%description -n noto-sans-carian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Carian Sans Serif font, hinted.

%package -n noto-sans-cham-fonts
Summary:        Noto Cham Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-cham
Provides:       noto-sans-cham

%description -n noto-sans-cham-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Cham Sans Serif font, hinted.

%package -n noto-sans-cherokee-fonts
Summary:        Noto Cherokee Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-cherokee
Provides:       noto-sans-cherokee

%description -n noto-sans-cherokee-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Cherokee Sans Serif font, hinted.

%package -n noto-sans-coptic-fonts
Summary:        Noto Coptic Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-coptic
Provides:       noto-sans-coptic

%description -n noto-sans-coptic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Coptic Sans Serif font, hinted.

%package -n noto-sans-cuneiform-fonts
Summary:        Noto Cuneiform Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-cuneiform
Provides:       noto-sans-cuneiform

%description -n noto-sans-cuneiform-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Cuneiform Sans Serif font, hinted.

%package -n noto-sans-cypriot-fonts
Summary:        Noto Cypriot Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-cypriot
Provides:       noto-sans-cypriot

%description -n noto-sans-cypriot-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Cypriot Sans Serif font, hinted.

%package -n noto-sans-deseret-fonts
Summary:        Noto Deseret Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-deseret
Provides:       noto-sans-deseret

%description -n noto-sans-deseret-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Deseret Sans Serif font, hinted.

%package -n noto-sans-devanagari-fonts
Summary:        Noto Devanagari Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-devanagari
Provides:       noto-sans-devanagari

%description -n noto-sans-devanagari-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Devanagari Sans Serif font, hinted.

%package -n noto-sans-egyptianhieroglyphs-fonts
Summary:        Noto Egyptian Hieroglyphs Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-egyptianhieroglyphs
Provides:       noto-sans-egyptianhieroglyphs

%description -n noto-sans-egyptianhieroglyphs-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
EgyptianHieroglyphs Sans Serif font, hinted.

%package -n noto-sans-ethiopic-fonts
Summary:        Noto Ethiopic Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-ethiopic
Provides:       noto-sans-ethiopic

%description -n noto-sans-ethiopic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Ethiopic Sans Serif font, hinted.

%package -n noto-sans-georgian-fonts
Summary:        Noto Georgian Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-georgian
Provides:       noto-sans-georgian

%description -n noto-sans-georgian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Georgian Sans Serif font, hinted.

%package -n noto-sans-glagolitic-fonts
Summary:        Noto Glagolitic Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-glagolitic
Provides:       noto-sans-glagolitic

%description -n noto-sans-glagolitic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Glagolitic Sans Serif font, hinted.

%package -n noto-sans-gothic-fonts
Summary:        Noto Gothic Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-gothic
Provides:       noto-sans-gothic

%description -n noto-sans-gothic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gothic Sans Serif font, hinted.

%package -n noto-sans-gujarati-fonts
Summary:        Noto Gujarati Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-gujarati
Provides:       noto-sans-gujarati

%description -n noto-sans-gujarati-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gujarati Sans Serif font, hinted.

%package -n noto-sans-gurmukhi-fonts
Summary:        Noto Gurmukhi Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-gurmukhi
Provides:       noto-sans-gurmukhi

%description -n noto-sans-gurmukhi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gurmukhi Sans Serif font, hinted.

%package -n noto-sans-hanunoo-fonts
Summary:        Noto Hanunoo Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-hanunoo
Provides:       noto-sans-hanunoo

%description -n noto-sans-hanunoo-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Hanunoo Sans Serif font, hinted.

%package -n noto-sans-hebrew-fonts
Summary:        Noto Hebrew Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-hebrew
Provides:       noto-sans-hebrew

%description -n noto-sans-hebrew-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Hebrew Sans Serif font, hinted.

%package -n noto-sans-imperialaramaic-fonts
Summary:        Noto Imperial Aramaic Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-imperialaramaic
Provides:       noto-sans-imperialaramaic

%description -n noto-sans-imperialaramaic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
ImperialAramaic Sans Serif font, hinted.

%package -n noto-sans-inscriptionalpahlavi-fonts
Summary:        Noto Inscriptional Pahlavi Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-inscriptionalpahlavi
Provides:       noto-sans-inscriptionalpahlavi

%description -n noto-sans-inscriptionalpahlavi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
InscriptionalPahlavi Sans Serif font, hinted.

%package -n noto-sans-inscriptionalparthian-fonts
Summary:        Noto Inscriptional Parthian Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-inscriptionalparthian
Provides:       noto-sans-inscriptionalparthian

%description -n noto-sans-inscriptionalparthian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
InscriptionalParthian Sans Serif font, hinted.

%package -n noto-sans-javanese-fonts
Summary:        Noto Javanese Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-javanese
Provides:       noto-sans-javanese

%description -n noto-sans-javanese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Javanese Sans Serif font, hinted.

%package -n noto-sans-kaithi-fonts
Summary:        Noto Kaithi Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-kaithi
Provides:       noto-sans-kaithi

%description -n noto-sans-kaithi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kaithi Sans Serif font, hinted.

%package -n noto-sans-kannada-fonts
Summary:        Noto Kannada Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-kannada
Provides:       noto-sans-kannada

%description -n noto-sans-kannada-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kannada Sans Serif font, hinted.

%package -n noto-sans-kayahli-fonts
Summary:        Noto Kayah Li Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-kayahli
Provides:       noto-sans-kayahli

%description -n noto-sans-kayahli-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
KayahLi Sans Serif font, hinted.

%package -n noto-sans-kharoshthi-fonts
Summary:        Noto Kharoshthi Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-kharoshthi
Provides:       noto-sans-kharoshthi

%description -n noto-sans-kharoshthi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kharoshthi Sans Serif font, hinted.

%package -n noto-sans-khmer-fonts
Summary:        Noto Khmer Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-khmer
Provides:       noto-sans-khmer

%description -n noto-sans-khmer-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Khmer Sans Serif font, hinted.

%package -n noto-sans-lao-fonts
Summary:        Noto Lao Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-lao
Provides:       noto-sans-lao

%description -n noto-sans-lao-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lao Sans Serif font, hinted.

%package -n noto-sans-lepcha-fonts
Summary:        Noto Lepcha Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-lepcha
Provides:       noto-sans-lepcha

%description -n noto-sans-lepcha-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lepcha Sans Serif font, hinted.

%package -n noto-sans-limbu-fonts
Summary:        Noto Limbu Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-limbu
Provides:       noto-sans-limbu

%description -n noto-sans-limbu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Limbu Sans Serif font, hinted.

%package -n noto-sans-linearb-fonts
Summary:        Noto Linear B Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-linearb
Provides:       noto-sans-linearb

%description -n noto-sans-linearb-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
LinearB Sans Serif font, hinted.

%package -n noto-sans-lisu-fonts
Summary:        Noto Lisu Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-lisu
Provides:       noto-sans-lisu

%description -n noto-sans-lisu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lisu Sans Serif font, hinted.

%package -n noto-sans-lycian-fonts
Summary:        Noto Lycian Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-lycian
Provides:       noto-sans-lycian

%description -n noto-sans-lycian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lycian Sans Serif font, hinted.

%package -n noto-sans-lydian-fonts
Summary:        Noto Lydian Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-lydian
Provides:       noto-sans-lydian

%description -n noto-sans-lydian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lydian Sans Serif font, hinted.

%package -n noto-sans-malayalam-fonts
Summary:        Noto Malayalam Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-malayalam
Provides:       noto-sans-malayalam

%description -n noto-sans-malayalam-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Malayalam Sans Serif font, hinted.

%package -n noto-sans-mandaic-fonts
Summary:        Noto Mandaic Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-mandaic
Provides:       noto-sans-mandaic

%description -n noto-sans-mandaic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Mandaic Sans Serif font, hinted.

%package -n noto-sans-meeteimayek-fonts
Summary:        Noto Meetei Mayek Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-meeteimayek
Provides:       noto-sans-meeteimayek

%description -n noto-sans-meeteimayek-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
MeeteiMayek Sans Serif font, hinted.

%package -n noto-sans-mongolian-fonts
Summary:        Noto Mongolian Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-mongolian
Provides:       noto-sans-mongolian

%description -n noto-sans-mongolian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Mongolian Sans Serif font, hinted.

%package -n noto-sans-myanmar-fonts
Summary:        Noto Myanmar Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-myanmar
Provides:       noto-sans-myanmar

%description -n noto-sans-myanmar-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Myanmar Sans Serif font, hinted.

%package -n noto-sans-nko-fonts
Summary:        Noto NKo Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-nko
Provides:       noto-sans-nko

%description -n noto-sans-nko-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NKo Sans Serif font, hinted.

%package -n noto-sans-newtailue-fonts
Summary:        Noto New TaiLue Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-newtailue
Provides:       noto-sans-newtailue

%description -n noto-sans-newtailue-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NewTaiLue Sans Serif font, hinted.

%package -n noto-sans-ogham-fonts
Summary:        Noto Ogham Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-ogham
Provides:       noto-sans-ogham

%description -n noto-sans-ogham-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Ogham Sans Serif font, hinted.

%package -n noto-sans-olchiki-fonts
Summary:        Noto Ol Chiki Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-olchiki
Provides:       noto-sans-olchiki

%description -n noto-sans-olchiki-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OlChiki Sans Serif font, hinted.

%package -n noto-sans-olditalic-fonts
Summary:        Noto Old Italic Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-olditalic
Provides:       noto-sans-olditalic

%description -n noto-sans-olditalic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldItalic Sans Serif font, hinted.

%package -n noto-sans-oldpersian-fonts
Summary:        Noto Old Persian Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-oldpersian
Provides:       noto-sans-oldpersian

%description -n noto-sans-oldpersian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldPersian Sans Serif font, hinted.

%package -n noto-sans-oldsoutharabian-fonts
Summary:        Noto Old SouthArabian Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-oldsoutharabian
Provides:       noto-sans-oldsoutharabian

%description -n noto-sans-oldsoutharabian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldSouthArabian Sans Serif font, hinted.

%package -n noto-sans-oldturkic-fonts
Summary:        Noto Old Turkic Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-oldturkic
Provides:       noto-sans-oldturkic

%description -n noto-sans-oldturkic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldTurkic Sans Serif font, hinted.

%package -n noto-sans-oriya-fonts
Summary:        Noto Oriya Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-oriya
Provides:       noto-sans-oriya

%description -n noto-sans-oriya-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Oriya Sans Serif font, hinted.

%package -n noto-sans-osmanya-fonts
Summary:        Noto Osmanya Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-osmanya
Provides:       noto-sans-osmanya

%description -n noto-sans-osmanya-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Osmanya Sans Serif font, hinted.

%package -n noto-sans-phagspa-fonts
Summary:        Noto Phags Pa Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-phagspa
Provides:       noto-sans-phagspa

%description -n noto-sans-phagspa-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
PhagsPa Sans Serif font, hinted.

%package -n noto-sans-phoenician-fonts
Summary:        Noto Phoenician Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-phoenician
Provides:       noto-sans-phoenician

%description -n noto-sans-phoenician-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Phoenician Sans Serif font, hinted.

%package -n noto-sans-rejang-fonts
Summary:        Noto Rejang Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-rejang
Provides:       noto-sans-rejang

%description -n noto-sans-rejang-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Rejang Sans Serif font, hinted.

%package -n noto-sans-runic-fonts
Summary:        Noto Runic Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-runic
Provides:       noto-sans-runic

%description -n noto-sans-runic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Runic Sans Serif font, hinted.

%package -n noto-sans-samaritan-fonts
Summary:        Noto Samaritan Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-samaritan
Provides:       noto-sans-samaritan

%description -n noto-sans-samaritan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Samaritan Sans Serif font, hinted.

%package -n noto-sans-saurashtra-fonts
Summary:        Noto Saurashtra Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-saurashtra
Provides:       noto-sans-saurashtra

%description -n noto-sans-saurashtra-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Saurashtra Sans Serif font, hinted.

%package -n noto-sans-shavian-fonts
Summary:        Noto Shavian Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-shavian
Provides:       noto-sans-shavian

%description -n noto-sans-shavian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Shavian Sans Serif font, hinted.

%package -n noto-sans-sinhala-fonts
Summary:        Noto Sinhala Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-sinhala
Provides:       noto-sans-sinhala

%description -n noto-sans-sinhala-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sinhala Sans Serif font, hinted.

%package -n noto-sans-sundanese-fonts
Summary:        Noto Sundanese Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-sundanese
Provides:       noto-sans-sundanese

%description -n noto-sans-sundanese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sundanese Sans Serif font, hinted.

%package -n noto-sans-sylotinagri-fonts
Summary:        Noto Syloti Nagri Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-sylotinagri
Provides:       noto-sans-sylotinagri

%description -n noto-sans-sylotinagri-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SylotiNagri Sans Serif font, hinted.

%package -n noto-sans-symbols-fonts
Summary:        Noto Symbols Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-symbols
Provides:       noto-sans-symbols

%description -n noto-sans-symbols-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Symbols Sans Serif font, hinted.

%package -n noto-sans-syriaceastern-fonts
Summary:        Noto Syriac Eastern Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-syriaceastern
Provides:       noto-sans-syriaceastern

%description -n noto-sans-syriaceastern-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SyriacEastern Sans Serif font, hinted.

%package -n noto-sans-syriacestrangela-fonts
Summary:        Noto Syriac Estrangela Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-syriacestrangela
Provides:       noto-sans-syriacestrangela

%description -n noto-sans-syriacestrangela-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SyriacEstrangela Sans Serif font, hinted.

%package -n noto-sans-syriacwestern-fonts
Summary:        Noto Syriac Western Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-syriacwestern
Provides:       noto-sans-syriacwestern

%description -n noto-sans-syriacwestern-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SyriacWestern Sans Serif font, hinted.

%package -n noto-sans-tagalog-fonts
Summary:        Noto Tagalog Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-tagalog
Provides:       noto-sans-tagalog

%description -n noto-sans-tagalog-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tagalog Sans Serif font, hinted.

%package -n noto-sans-tagbanwa-fonts
Summary:        Noto Tagbanwa Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-tagbanwa
Provides:       noto-sans-tagbanwa

%description -n noto-sans-tagbanwa-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tagbanwa Sans Serif font, hinted.

%package -n noto-sans-taile-fonts
Summary:        Noto Tai Le Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-taile
Provides:       noto-sans-taile

%description -n noto-sans-taile-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TaiLe Sans Serif font, hinted.

%package -n noto-sans-taitham-fonts
Summary:        Noto Tai Tham Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-taitham
Provides:       noto-sans-taitham

%description -n noto-sans-taitham-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TaiTham Sans Serif font, hinted.

%package -n noto-sans-taiviet-fonts
Summary:        Noto Tai Viet Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-taiviet
Provides:       noto-sans-taiviet

%description -n noto-sans-taiviet-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TaiViet Sans Serif font, hinted.

%package -n noto-sans-tamil-fonts
Summary:        Noto Tamil Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-tamil
Provides:       noto-sans-tamil

%description -n noto-sans-tamil-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tamil Sans Serif font, hinted.

%package -n noto-sans-telugu-fonts
Summary:        Noto Telugu Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-telugu
Provides:       noto-sans-telugu

%description -n noto-sans-telugu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Telugu Sans Serif font, hinted.

%package -n noto-sans-thaana-fonts
Summary:        Noto Thaana Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-thaana
Provides:       noto-sans-thaana

%description -n noto-sans-thaana-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Thaana Sans Serif font, hinted.

%package -n noto-sans-thai-fonts
Summary:        Noto Thai Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-thai
Provides:       noto-sans-thai

%description -n noto-sans-thai-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Thai Sans Serif font, hinted.

%package -n noto-sans-tibetan-fonts
Summary:        Noto Tibetan Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-tibetan
Provides:       noto-sans-tibetan

%description -n noto-sans-tibetan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tibetan Sans Serif font, hinted.

%package -n noto-sans-tifinagh-fonts
Summary:        Noto Tifinagh Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-tifinagh
Provides:       noto-sans-tifinagh

%description -n noto-sans-tifinagh-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tifinagh Sans Serif font, hinted.

%package -n noto-sans-ugaritic-fonts
Summary:        Noto Ugaritic Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-ugaritic
Provides:       noto-sans-ugaritic

%description -n noto-sans-ugaritic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Ugaritic Sans Serif font, hinted.

%package -n noto-sans-vai-fonts
Summary:        Noto Vai Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-vai
Provides:       noto-sans-vai

%description -n noto-sans-vai-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Vai Sans Serif font, hinted.

%package -n noto-sans-yi-fonts
Summary:        Noto Yi Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-sans-yi
Provides:       noto-sans-yi

%description -n noto-sans-yi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Yi Sans Serif font, hinted.

%package -n noto-serif-fonts
Summary:        Noto  Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-serif
Provides:       noto-serif

%description -n noto-serif-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
 Sans Serif font, hinted.

%package -n noto-serif-armenian-fonts
Summary:        Noto Armenian Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-serif-armenian
Provides:       noto-serif-armenian

%description -n noto-serif-armenian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Armenian Sans Serif font, hinted.

%package -n noto-serif-georgian-fonts
Summary:        Noto Georgian Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-serif-georgian
Provides:       noto-serif-georgian

%description -n noto-serif-georgian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Georgian Sans Serif font, hinted.

%package -n noto-serif-khmer-fonts
Summary:        Noto Khmer Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-serif-khmer
Provides:       noto-serif-khmer

%description -n noto-serif-khmer-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Khmer Sans Serif font, hinted.

%package -n noto-serif-lao-fonts
Summary:        Noto Lao Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-serif-lao
Provides:       noto-serif-lao

%description -n noto-serif-lao-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lao Sans Serif font, hinted.

%package -n noto-serif-thai-fonts
Summary:        Noto Thai Sans Serif Font
Group:          System/Fonts/True type
Requires:       google-noto-fonts-doc
Obsoletes:      noto-serif-thai
Provides:       noto-serif-thai

%description -n noto-serif-thai-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Thai Sans Serif font, hinted.



%prep
%setup -q -c -n %{name}-%{version}
rm -f *Draft.*tf
# use otc file for CJK
rm -f NotoSans*CJK*.otf
unzip -o %{S:1}

%build

%install
install -m 0755 -d %{buildroot}%{_ttfontsdir}
install -m 0644 -p *.ttf %{buildroot}%{_ttfontsdir}
install -m 0644 -p *.ttc %{buildroot}%{_ttfontsdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/59-noto-sans-cjk-fontconfig.conf

ln -s %{_fontconfig_templatedir}/59-noto-sans-cjk-fontconfig.conf \
      %{buildroot}%{_fontconfig_confdir}/59-noto-sans-cjk-fontconfig.conf




%files doc
%doc LICENSE*.txt

%files -n noto-coloremoji-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoColorEmoji*.?tf

%files -n noto-emoji-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoEmoji-*.?tf

%files -n noto-kufiarabic-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoKufiArabic-*.?tf

%files -n noto-naskharabic-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoNaskhArabic-*.?tf

%files -n noto-nastaliqurdu-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoNastaliqUrdu-*.?tf

%files -n noto-sans-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSans-*.?tf

%files -n noto-sans-armenian-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansArmenian-*.?tf

%files -n noto-sans-avestan-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansAvestan-*.?tf

%files -n noto-sans-balinese-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBalinese-*.?tf

%files -n noto-sans-bamum-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBamum-*.?tf

%files -n noto-sans-batak-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBatak-*.?tf

%files -n noto-sans-bengali-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBengali-*.?tf

%files -n noto-sans-brahmi-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBrahmi-*.?tf

%files -n noto-sans-buginese-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBuginese-*.?tf

%files -n noto-sans-buhid-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBuhid-*.?tf

%files -n noto-sans-cjk-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJK*.ttc
%{_fontconfig_templatedir}/59*.conf
%config(noreplace) %{_fontconfig_confdir}/59*.conf

%files -n noto-sans-canadianaboriginal-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCanadianAboriginal-*.?tf

%files -n noto-sans-carian-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCarian-*.?tf

%files -n noto-sans-cham-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCham-*.?tf

%files -n noto-sans-cherokee-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCherokee-*.?tf

%files -n noto-sans-coptic-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCoptic-*.?tf

%files -n noto-sans-cuneiform-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCuneiform-*.?tf

%files -n noto-sans-cypriot-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCypriot-*.?tf

%files -n noto-sans-deseret-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansDeseret-*.?tf

%files -n noto-sans-devanagari-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansDevanagari-*.?tf

%files -n noto-sans-egyptianhieroglyphs-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansEgyptianHieroglyphs-*.?tf

%files -n noto-sans-ethiopic-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansEthiopic-*.?tf

%files -n noto-sans-georgian-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGeorgian-*.?tf

%files -n noto-sans-glagolitic-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGlagolitic-*.?tf

%files -n noto-sans-gothic-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGothic-*.?tf

%files -n noto-sans-gujarati-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGujarati-*.?tf

%files -n noto-sans-gurmukhi-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGurmukhi-*.?tf

%files -n noto-sans-hanunoo-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHanunoo-*.?tf

%files -n noto-sans-hebrew-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHebrew-*.?tf

%files -n noto-sans-imperialaramaic-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansImperialAramaic-*.?tf

%files -n noto-sans-inscriptionalpahlavi-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansInscriptionalPahlavi-*.?tf

%files -n noto-sans-inscriptionalparthian-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansInscriptionalParthian-*.?tf

%files -n noto-sans-javanese-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansJavanese-*.?tf

%files -n noto-sans-kaithi-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKaithi-*.?tf

%files -n noto-sans-kannada-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKannada-*.?tf

%files -n noto-sans-kayahli-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKayahLi-*.?tf

%files -n noto-sans-kharoshthi-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKharoshthi-*.?tf

%files -n noto-sans-khmer-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKhmer-*.?tf

%files -n noto-sans-lao-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLao-*.?tf

%files -n noto-sans-lepcha-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLepcha-*.?tf

%files -n noto-sans-limbu-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLimbu-*.?tf

%files -n noto-sans-linearb-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLinearB-*.?tf

%files -n noto-sans-lisu-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLisu-*.?tf

%files -n noto-sans-lycian-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLycian-*.?tf

%files -n noto-sans-lydian-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLydian-*.?tf

%files -n noto-sans-malayalam-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMalayalam-*.?tf

%files -n noto-sans-mandaic-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMandaic-*.?tf

%files -n noto-sans-meeteimayek-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMeeteiMayek-*.?tf

%files -n noto-sans-mongolian-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMongolian-*.?tf

%files -n noto-sans-myanmar-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMyanmar-*.?tf

%files -n noto-sans-nko-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNKo-*.?tf

%files -n noto-sans-newtailue-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNewTaiLue-*.?tf

%files -n noto-sans-ogham-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOgham-*.?tf

%files -n noto-sans-olchiki-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOlChiki-*.?tf

%files -n noto-sans-olditalic-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldItalic-*.?tf

%files -n noto-sans-oldpersian-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldPersian-*.?tf

%files -n noto-sans-oldsoutharabian-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldSouthArabian-*.?tf

%files -n noto-sans-oldturkic-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldTurkic-*.?tf

%files -n noto-sans-oriya-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOriya-*.?tf

%files -n noto-sans-osmanya-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOsmanya-*.?tf

%files -n noto-sans-phagspa-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansPhagsPa-*.?tf

%files -n noto-sans-phoenician-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansPhoenician-*.?tf

%files -n noto-sans-rejang-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansRejang-*.?tf

%files -n noto-sans-runic-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansRunic-*.?tf

%files -n noto-sans-samaritan-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSamaritan-*.?tf

%files -n noto-sans-saurashtra-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSaurashtra-*.?tf

%files -n noto-sans-shavian-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansShavian-*.?tf

%files -n noto-sans-sinhala-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSinhala-*.?tf

%files -n noto-sans-sundanese-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSundanese-*.?tf

%files -n noto-sans-sylotinagri-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSylotiNagri-*.?tf

%files -n noto-sans-symbols-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSymbols-*.?tf

%files -n noto-sans-syriaceastern-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSyriacEastern-*.?tf

%files -n noto-sans-syriacestrangela-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSyriacEstrangela-*.?tf

%files -n noto-sans-syriacwestern-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSyriacWestern-*.?tf

%files -n noto-sans-tagalog-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTagalog-*.?tf

%files -n noto-sans-tagbanwa-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTagbanwa-*.?tf

%files -n noto-sans-taile-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTaiLe-*.?tf

%files -n noto-sans-taitham-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTaiTham-*.?tf

%files -n noto-sans-taiviet-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTaiViet-*.?tf

%files -n noto-sans-tamil-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTamil-*.?tf

%files -n noto-sans-telugu-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTelugu-*.?tf

%files -n noto-sans-thaana-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansThaana-*.?tf

%files -n noto-sans-thai-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansThai-*.?tf

%files -n noto-sans-tibetan-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTibetan-*.?tf

%files -n noto-sans-tifinagh-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTifinagh-*.?tf

%files -n noto-sans-ugaritic-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansUgaritic-*.?tf

%files -n noto-sans-vai-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansVai-*.?tf

%files -n noto-sans-yi-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansYi-*.?tf

%files -n noto-serif-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerif-*.?tf

%files -n noto-serif-armenian-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifArmenian-*.?tf

%files -n noto-serif-georgian-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifGeorgian-*.?tf

%files -n noto-serif-khmer-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifKhmer-*.?tf

%files -n noto-serif-lao-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifLao-*.?tf

%files -n noto-serif-thai-fonts
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifThai-*.?tf




