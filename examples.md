# TogoDX/Human

## Gene
### Gene biotype

- [miRNAに原因のある遺伝性疾患](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%5D&values=%5B%7B%22attributeId%22%3A%22gene_biotype_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22miRNA%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22disease_diseases_mondo%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%220003847%22%7D%5D%7D%5D) (Ensembl gene 3件)
    - MIR96, MIR140, MIR204 (難聴, 脊椎骨端異形成症, 網膜ジストロフィー)
        - MIR96 ENSG00000199158 Autosomal dominant non-syndromic sensorineural deafness type DFNA
        - MIR140 ENSG00000208017 Spondyloepiphyseal dysplasia, Nishimura type
        - MIR204 ENSG00000207935 Familial progressive retinal dystrophy-iris coloboma-congenital cataract syndrome

### Chromosome

- [Y染色体の遺伝子が特異的に発現している組織を見る](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22gene_high_level_expression_refex%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2224%22%7D%5D%7D%5D) (Ensembl gene 521件)
    - Testis特異的発現が多い
    - ところで, Cerebellum(小脳)特異的に発現しているNLGN4Yという遺伝子があるが ([link](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2224%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22gene_high_level_expression_refex%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22v02_40%22%7D%5D%7D%5D)), これは女性では発現していないということ? -> X染色体に対応するNLGN4Xというのがあるらしい. 新しい性タイピング遺伝子として提案された. ([link](https://pubmed.ncbi.nlm.nih.gov/31852540/))
    - targtをNCBI geneにすると285件になるのはなぜ?

- [Y染色体の遺伝子は、どのような病気に関連しているか](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2224%22%7D%5D%7D%5D)
    - 1件ヒット: SRY遺伝子 (sex determining region Y)
- [神経系疾患に関連する遺伝子が、どの染色体にあるか](https://togodx.dbcls.jp/human/?togoKey=mesh&keys=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22D009422%22%7D%5D%7D%5D)
- [MTゲノムにコードされているタンパク質は、構造が決まっているか](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22structure_data_existence_uniprot%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2225%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22gene_biotype_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22protein_coding%22%7D%5D%7D%5D) (Ensembl gene 13件)
    - 構造が決まっているものが比較的多い (11件). 決まっていないものが2つあるが (MT-ATP6, MT-ATP8) , この2つも重要なものらしい. ([link](http://grj.umin.jp/grj/mt-overview.htm)).
    - ターゲットをPDBにしたときに出てくるラベルにWaterとかが出てくるのはバグ
    - PDBについてmetastanza API error

### # of paralogs

- [singletonをターゲットとしてmetabolic diseasesに効く薬](https://togodx.dbcls.jp/human/?togoKey=chebi&keys=%5B%5D&values=%5B%7B%22attributeId%22%3A%22gene_number_of_paralogs_homologene%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22paralog_count_01%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%221%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22disease_diseases_mesh%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22D008659%22%2C%22ancestors%22%3A%5B%22D009750%22%5D%7D%5D%7D%5D)

### Evolutionary divergence

- [zinc-fingerドメイン持ち、そのオルソログがマウスやラットにあるタンパク質をターゲットとする薬](https://togodx.dbcls.jp/human/?togoKey=chebi&keys=%5B%5D&values=%5B%7B%22attributeId%22%3A%22gene_evolutionary_conservation_homologene%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22branch_04%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22protein_domains_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22863%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%221%22%7D%5D%7D%5D)

### Tissue-specific high expression (RefEx GeneChip)

- [環境汚染物質がターゲットとする遺伝子がどこで高発現しているか](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22gene_high_level_expression_refex%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22compound_chemical_role_chebi%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2278298%22%7D%5D%7D%5D)

### Tissue-specific low expression (RefEx GeneChip)

- [Y染色体の遺伝子の発現特異性](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22gene_low_level_expression_refex%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2224%22%7D%5D%7D%5D)

### Tissue-specific high expression (GTEx)

- [Y染色体の遺伝子の発現特異性](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22gene_not_expressed_in_tissues_gtex%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2224%22%7D%5D%7D%5D)

### No expression in tissues (GTEx)

- [Y染色体の遺伝子の発現特異性](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22gene_specific_expression_in_tissues_hpa%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2224%22%7D%5D%7D%5D)

### Tissue-specific high expression (HPA)

- [Y染色体の遺伝子の発現特異性](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22gene_specific_expression_in_tissues_hpa%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2224%22%7D%5D%7D%5D)

### Cell type-specific high expression (HPA)

- [Y染色体の遺伝子の発現特異性](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22gene_specific_expression_in_cells_hpa%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2224%22%7D%5D%7D%5D)

## Protein

### Protein domains

- [免疫グロブリンドメインを持つタンパク質をコードする遺伝子のGO(Biological process)一覧](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22protein_biological_process_uniprot%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22protein_domains_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22393%22%7D%5D%7D%5D)

### Cellular component

- [ミトコンドリアゲノムにコードされたタンパク質の細胞内局在](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22protein_cellular_component_uniprot%22%2C%22id%22%3A%7B%22categoryId%22%3A%22GO_0110165%22%2C%22ancestors%22%3A%5B%5D%7D%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2225%22%7D%5D%7D%5D)

### Biological process

- [免疫グロブリンドメインを持つタンパク質をコードする遺伝子のGO(Biological process)一覧](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22protein_biological_process_uniprot%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22protein_domains_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22393%22%7D%5D%7D%5D)
    - timeout of 120000ms exceeded になる → 高速化版ではタイムアウトしなくなっていた

### Molecular function

- [ミトコンドリアゲノムにコードされた遺伝子のGO(Molecular function)](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22protein_molecular_function_uniprot%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2225%22%7D%5D%7D%5D)

### Ligands

- [DNA結合型転写因子として組織特異的に高発現し、Zincと結合･反応して機能するタンパク質の一覧](https://togodx.dbcls.jp/human/?togoKey=uniprot&keys=%5B%7B%22attributeId%22%3A%22gene_high_level_expression_refex%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22protein_molecular_function_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22GO_0003700%22%2C%22ancestors%22%3A%5B%22GO_0140110%22%5D%7D%5D%7D%2C%7B%22attributeId%22%3A%22protein_ligands_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22862%22%7D%5D%7D%5D)　(955個)
    

### Molecular mass

- [分子量が100kDa以上でDNA結合型転写因子として組織特異的に高発現し、Zincと結合･反応して機能するタンパク質の一覧](https://togodx.dbcls.jp/human/?togoKey=uniprot&keys=%5B%7B%22attributeId%22%3A%22gene_high_level_expression_refex%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22protein_molecular_function_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22GO_0003700%22%2C%22ancestors%22%3A%5B%22GO_0140110%22%5D%7D%5D%7D%2C%7B%22attributeId%22%3A%22protein_molecular_mass_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2211%22%7D%2C%7B%22categoryId%22%3A%2212%22%7D%2C%7B%22categoryId%22%3A%2213%22%7D%2C%7B%22categoryId%22%3A%2214%22%7D%2C%7B%22categoryId%22%3A%2215%22%7D%2C%7B%22categoryId%22%3A%2216%22%7D%2C%7B%22categoryId%22%3A%2217%22%7D%2C%7B%22categoryId%22%3A%2218%22%7D%2C%7B%22categoryId%22%3A%2219%22%7D%2C%7B%22categoryId%22%3A%2220%22%7D%2C%7B%22categoryId%22%3A%2221%22%7D%2C%7B%22categoryId%22%3A%2222%22%7D%2C%7B%22categoryId%22%3A%2223%22%7D%2C%7B%22categoryId%22%3A%2224%22%7D%2C%7B%22categoryId%22%3A%2225%22%7D%2C%7B%22categoryId%22%3A%2226%22%7D%2C%7B%22categoryId%22%3A%2227%22%7D%2C%7B%22categoryId%22%3A%2228%22%7D%2C%7B%22categoryId%22%3A%2229%22%7D%2C%7B%22categoryId%22%3A%2230%22%7D%2C%7B%22categoryId%22%3A%2231%22%7D%2C%7B%22categoryId%22%3A%2232%22%7D%2C%7B%22categoryId%22%3A%2233%22%7D%2C%7B%22categoryId%22%3A%2234%22%7D%2C%7B%22categoryId%22%3A%2235%22%7D%2C%7B%22categoryId%22%3A%2236%22%7D%2C%7B%22categoryId%22%3A%2237%22%7D%2C%7B%22categoryId%22%3A%2238%22%7D%2C%7B%22categoryId%22%3A%2239%22%7D%2C%7B%22categoryId%22%3A%2240%22%7D%2C%7B%22categoryId%22%3A%2241%22%7D%2C%7B%22categoryId%22%3A%2242%22%7D%2C%7B%22categoryId%22%3A%2243%22%7D%2C%7B%22categoryId%22%3A%2244%22%7D%2C%7B%22categoryId%22%3A%2245%22%7D%2C%7B%22categoryId%22%3A%2246%22%7D%2C%7B%22categoryId%22%3A%2247%22%7D%2C%7B%22categoryId%22%3A%2248%22%7D%2C%7B%22categoryId%22%3A%2249%22%7D%2C%7B%22categoryId%22%3A%2250%22%7D%2C%7B%22categoryId%22%3A%2251%22%7D%2C%7B%22categoryId%22%3A%2252%22%7D%2C%7B%22categoryId%22%3A%2253%22%7D%2C%7B%22categoryId%22%3A%2254%22%7D%2C%7B%22categoryId%22%3A%2255%22%7D%2C%7B%22categoryId%22%3A%2256%22%7D%2C%7B%22categoryId%22%3A%2257%22%7D%2C%7B%22categoryId%22%3A%2258%22%7D%2C%7B%22categoryId%22%3A%2259%22%7D%2C%7B%22categoryId%22%3A%2260%22%7D%2C%7B%22categoryId%22%3A%2262%22%7D%2C%7B%22categoryId%22%3A%2263%22%7D%2C%7B%22categoryId%22%3A%2264%22%7D%2C%7B%22categoryId%22%3A%2265%22%7D%2C%7B%22categoryId%22%3A%2270%22%7D%2C%7B%22categoryId%22%3A%2273%22%7D%2C%7B%22categoryId%22%3A%2274%22%7D%2C%7B%22categoryId%22%3A%2278%22%7D%2C%7B%22categoryId%22%3A%2279%22%7D%2C%7B%22categoryId%22%3A%2280%22%7D%2C%7B%22categoryId%22%3A%2281%22%7D%2C%7B%22categoryId%22%3A%2284%22%7D%2C%7B%22categoryId%22%3A%2285%22%7D%2C%7B%22categoryId%22%3A%2286%22%7D%2C%7B%22categoryId%22%3A%2287%22%7D%2C%7B%22categoryId%22%3A%2289%22%7D%2C%7B%22categoryId%22%3A%2297%22%7D%2C%7B%22categoryId%22%3A%2298%22%7D%2C%7B%22categoryId%22%3A%22101%22%7D%2C%7B%22categoryId%22%3A%22102%22%7D%2C%7B%22categoryId%22%3A%22152%22%7D%2C%7B%22categoryId%22%3A%22302%22%7D%2C%7B%22categoryId%22%3A%22382%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22protein_ligands_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22862%22%7D%5D%7D%5D)　(91個)


### PTMs

- [Viral processに関わり、Glycoprotein(糖タンパク質)の翻訳後修飾を受けるタンパク質のうち、組織別に結合する糖鎖の種類が明らかになっているかを調べる(かつ、それらの遺伝子の組織における発現状況を調べる)。](https://togodx.dbcls.jp/human/?togoKey=uniprot&keys=%5B%7B%22attributeId%22%3A%22glycan_tissue_glycosmos%22%7D%2C%7B%22attributeId%22%3A%22gene_high_level_expression_refex%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22protein_ptms_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22325%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22protein_biological_process_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22GO_0016032%22%7D%5D%7D%5D)　(135個)
    
    - このAttributeの問題ではないが、GlyTouCanのデータは、EGFR、CD4、MMP1、ITB1、PTPRCのみが表示されており、いずれもN/Aの表記になっている
        - N/Aの意味はどの組織で結合するか明確にはなっていない、という解釈で合っている?
        - 残りの130個はGlyTouCanのデータがないが、これは結合する糖鎖が調べられていないということ?

### # of transmembrane domains

- [Gタンパク質共役型ペプチドレセプタータンパク質の膜貫通型ドメインの数とそれらの立体構造データの有無](https://togodx.dbcls.jp/human/?togoKey=uniprot&keys=%5B%7B%22attributeId%22%3A%22protein_number_of_transmembrane_domains_uniprot%22%7D%2C%7B%22attributeId%22%3A%22structure_data_existence_uniprot%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22protein_molecular_function_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22GO_0008528%22%2C%22ancestors%22%3A%5B%22GO_0060089%22%2C%22GO_0038023%22%2C%22GO_0004888%22%2C%22GO_0004930%22%5D%7D%5D%7D%5D)　(212個)
    

### # of phosphorylation sites

- [タンパク質ポリンについて、リン酸化部位の数、膜貫通型ドメインの数、および局在を見る](https://togodx.dbcls.jp/human/?togoKey=uniprot&keys=%5B%7B%22attributeId%22%3A%22protein_number_of_transmembrane_domains_uniprot%22%7D%2C%7B%22attributeId%22%3A%22protein_number_of_phosphorylation_sites_uniprot%22%7D%2C%7B%22attributeId%22%3A%22protein_cellular_component_uniprot%22%2C%22id%22%3A%7B%22categoryId%22%3A%22GO_0016020%22%2C%22ancestors%22%3A%5B%22GO_0110165%22%5D%7D%7D%5D&values=%5B%7B%22attributeId%22%3A%22protein_domains_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22626%22%2C%22ancestors%22%3A%5B%22812%22%5D%7D%5D%7D%5D) (UniProt 16件)

### # of glycosylation sites

- [免疫グロブリンドメインを持つタンパク質について、糖鎖修飾部位の数、リン酸化部位の数、膜貫通型ドメインの数を見る](https://togodx.dbcls.jp/human/?togoKey=uniprot&keys=%5B%7B%22attributeId%22%3A%22protein_number_of_glycosylation_sites_uniprot%22%7D%2C%7B%22attributeId%22%3A%22protein_number_of_phosphorylation_sites_uniprot%22%7D%2C%7B%22attributeId%22%3A%22protein_number_of_transmembrane_domains_uniprot%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22protein_domains_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22393%22%7D%5D%7D%5D) (UniProt 886件)


### Disease-related proteins

- [Y染色体にある遺伝子は、どのような病気に関連しているか](https://togodx-attribute-g3.dbcls.jp/human/?togoKey=uniprot&keys=%5B%7B%22attributeId%22%3A%22protein_disease_related_proteins_uniprot%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2224%22%7D%5D%7D%5D) (UniProt 92件)
    - Unclassified 82, Deafness 1, Disease variant 1

### Tissues w/expression reported

- [Y染色体の遺伝子の発現特異性](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22protein_isolation_source_uniprot%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2224%22%7D%5D%7D%5D)
    - timeout of 120000ms exceeded になる→高速化版ではタイムアウトしなくなっていた

### Evidence of existence

- [ホモロジーから存在が推測されるタンパク質は、どの染色体にコードされていて、どんなドメインを持っているか](https://togodx.dbcls.jp/human/?togoKey=uniprot&keys=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%7D%2C%7B%22attributeId%22%3A%22protein_domains_uniprot%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22protein_evidence_of_existence_nextprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%223%22%7D%5D%7D%5D) (UniProt 147件)
    - 11番染色体に多く、膜貫通型ドメインが多い

## Structure

### Structure data existence

- [構造を持つタンパク質と遺伝子の染色体ごとの分布](https://togodx.dbcls.jp/human/?togoKey=pdb&keys=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22structure_data_existence_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%221%22%7D%5D%7D%5D)
- [疾患に関連する構造タンパク質と遺伝子の染色体ごとの分布](https://togodx.dbcls.jp/human/?togoKey=mondo&keys=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22structure_data_existence_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%221%22%7D%5D%7D%5D)
- Attributeの課題有り
    - 現在、構造データが有る･無いの2択になっているが、PDBのデータが合っても部分構造の場合が多い。完全に構造が決まっているもの、部分的に決まっているもの(その割合別とか?)、構造データが一つもないもの、のように属性が分かれていると有用性が上がりそう(小野)
    - 井出さんがPDB各エントリに紐付いている構造データの数を取る[クエリを作成](https://is.gd/og05wa)している
        - 現在の構造データ有りの7299エントリをさらに160くらいに分類できそう
        - https://togodx.integbio.jp/sparqlist_dev/structure_data_existence_uniprot_num

### # of alpha-helices

- [GWASでアルツハイマー病に関連付けられた遺伝子について, PDBのαヘリックス数の分布](https://togodx.dbcls.jp/human/?togoKey=uniprot&keys=%5B%7B%22attributeId%22%3A%22structure_number_of_alpha_helices_pdb%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22variant_gwas_togovar%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22EFO_0009268%22%2C%22ancestors%22%3A%5B%22IAO_0000030%22%2C%22EFO_0000352%22%2C%22EFO_0000493%22%5D%7D%5D%7D%5D)
    - 12と32にピークがある → 解釈は可能か?
- [GWASでアルツハイマー病に関連付けられた遺伝子について, PDBのαヘリックス数の分布 (UniProtバージョン)](https://sparql-support.dbcls.jp/dxs/build/?togoKey=uniprot&keys=%5B%7B%22attributeId%22%3A%22protein_number_of_helix_uniprot%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22protein_domains_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22812%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22variant_gwas_togovar%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22EFO_0009268%22%2C%22ancestors%22%3A%5B%22IAO_0000030%22%2C%22EFO_0000352%22%2C%22EFO_0000493%22%5D%7D%5D%7D%2C%7B%22attributeId%22%3A%22protein_reviewed_flag_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22reviewed%22%7D%5D%7D%5D)
    - ヘリックスの数が63と一番多いのは、ACEという遺伝子
    - ログスケールにしないと分布がわかりにくい?
- ソースをPDBからUniProtに変える(井出さん)

### # of beta-sheets

- [GWASでアルツハイマー病に関連付けられた遺伝子について, PDBのβシート数の分布](https://togodx.dbcls.jp/human/?togoKey=uniprot&keys=%5B%7B%22attributeId%22%3A%22structure_number_of_beta_sheets_pdb%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22variant_gwas_togovar%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22EFO_0009268%22%2C%22ancestors%22%3A%5B%22IAO_0000030%22%2C%22EFO_0000352%22%2C%22EFO_0000493%22%5D%7D%5D%7D%5D)
    - 0,3,4にピーク
- ソースをPDBからUniProtに変える(井出さん)

### # of peptides in a PDB entry

- [Y染色体上の遺伝子がコードするタンパク質が持つペプチドの数](https://togodx.dbcls.jp/human/?togoKey=uniprot&keys=%5B%7B%22attributeId%22%3A%22structure_number_of_peptides_pdb%22%7D%2C%7B%22attributeId%22%3A%22structure_data_existence_uniprot%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2224%22%7D%5D%7D%5D)
    - データとしては正しそう
    - ペプチドの数は、実験手法的に前例のあるダイマーや複合体などを形成していそうだというのはわかる

### Analysis methods

- [Neutron diffraction(中性子回折法)を使って同定したPDBエントリに関連する疾患と遺伝子の染色体ごとの分布](https://togodx.dbcls.jp/human/?togoKey=nando&keys=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22structure_analysis_methods_pdb%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2204%22%7D%5D%7D%5D)

## Interaction

### Proteins in pathway

- [目的の反応にcomponentとして参加する化合物とタンパク質をリストし、そのタンパク質の構造が解析されているかどうかを調べる](https://togodx.dbcls.jp/human/?togoKey=chebi&keys=%5B%7B%22attributeId%22%3A%22structure_data_existence_uniprot%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22interaction_proteins_in_pathway_reactome%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22R-HSA-2162123%22%2C%22ancestors%22%3A%5B%22R-HSA-1430728%22%2C%22R-HSA-556833%22%2C%22R-HSA-8978868%22%2C%22R-HSA-2142753%22%5D%7D%5D%7D%2C%7B%22attributeId%22%3A%22interaction_compounds_in_pathway_reactome%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22R-HSA-2162123%22%2C%22ancestors%22%3A%5B%22R-HSA-1430728%22%2C%22R-HSA-556833%22%2C%22R-HSA-8978868%22%2C%22R-HSA-2142753%22%5D%7D%5D%7D%5D)

### Compounds in pathway

- [目的の反応にcomponentとして参加する化合物とタンパク質をリストし、そのタンパク質の構造が解析されているかどうかを調べる](https://togodx.dbcls.jp/human/?togoKey=chebi&keys=%5B%7B%22attributeId%22%3A%22structure_data_existence_uniprot%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22interaction_proteins_in_pathway_reactome%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22R-HSA-2162123%22%2C%22ancestors%22%3A%5B%22R-HSA-1430728%22%2C%22R-HSA-556833%22%2C%22R-HSA-8978868%22%2C%22R-HSA-2142753%22%5D%7D%5D%7D%2C%7B%22attributeId%22%3A%22interaction_compounds_in_pathway_reactome%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22R-HSA-2162123%22%2C%22ancestors%22%3A%5B%22R-HSA-1430728%22%2C%22R-HSA-556833%22%2C%22R-HSA-8978868%22%2C%22R-HSA-2142753%22%5D%7D%5D%7D%5D)

### # of interacting proteins

- [Infectionsに関わる化合物が相互作用するタンパク質の数を知りたい](https://togodx.dbcls.jp/human/?togoKey=chembl_compound&keys=%5B%7B%22attributeId%22%3A%22interaction_number_of_interacting_proteins_uniprot%22%7D%2C%7B%22attributeId%22%3A%22interaction_chembl_assay_existence_uniprot%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22D007239%22%7D%5D%7D%5D)
    - 化合物 -> タンパク質のパスに懸念あり

### ChEMBL assay existence

- [ミトコンドリアゲノム由来のタンパク質をターゲットとする薬とその適用疾患](https://togodx.dbcls.jp/human/?togoKey=chebi&keys=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2225%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%221%22%7D%5D%7D%5D)
- [どう働くかよくわかっていないけれど薬効が認められている物質](https://togodx.dbcls.jp/human/?togoKey=mesh&keys=%5B%5D&values=%5B%7B%22attributeId%22%3A%22compound_application_type_chebi%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2252217%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22unclassified%22%7D%5D%7D%5D)
    - 504 Gateway Timeout → 高速化版では動くようになっていた.

## Compound

- Compound全般について、他のカテゴリーのIDとの関係がよく見えないので意味の解釈が難しい
- （案としては）ルートを１つに絞る？

### Chemical role

- [環境汚染物質がターゲットとする遺伝子がどこで高発現しているか](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22gene_high_level_expression_refex%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22compound_chemical_role_chebi%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2278298%22%7D%5D%7D%5D)
    - target: CHEBI compound : 1240件
    - 下図最初のTarget（ラベルがNull）を選ぶとMetaStanza API error SyntaxError: Unexpected token T in JSON at position 0 となる

- [疾患に関与する環境汚染物質](https://togodx.dbcls.jp/human/?togoKey=chebi&keys=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22compound_chemical_role_chebi%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2278298%22%7D%5D%7D%5D)
    - target:ChEBI compound: 353件
    - Chemical CompoundとDiseases in MeSHはChEMBL Drug Indicationを通してつながっているはずなので、疾患に薬効を持つ環境汚染物質という意味になると思われるが、それがわかりにくい


- [環境汚染物質が薬として役立つ疾患](https://togodx.dbcls.jp/human/?togoKey=mesh&keys=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22compound_chemical_role_chebi%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2278298%22%7D%5D%7D%5D)
    - target: Disease in MeSH: 803 件
        - target のみ MONDOに変えると605, NANDOに変えると0, HPOに変えると80
    - Chemical CompoundとDiseases in MeSHの関係については上と同じ。「環境汚染物質」と「疾患」の関係だと、つい、物質が引き起こす疾患、と考えてしまうので混乱する
        - 化学物質とそれが引き起こす疾患の関係について、**[Comparative Toxicogenomics Database](http://ctdbase.org/)**に[ダウンロード可能なデータ](http://ctdbase.org/downloads/)がある（*subject to [certain terms](http://ctdbase.org/about/legal.jsp)*）のを見つけた（既知だったらすみません）。物質がMeSHのUIDで参照されている。例：エタノールならD000431
            - PubChem/ChEMBL/ChEBIから[MeSH Tree](https://meshb.nlm.nih.gov/treeView)のChemicals and Drugs [D] へのマッピングが必要になる。現状、Diseases [C]へマップしている。（TogoIDも：PubChem CID:702を入れてもMeSH:D000431は出てきません。これはこれで問題かも）

### Application type

- [薬効のある化粧品（香料含む）](https://togodx.dbcls.jp/human/?togoKey=pubchem_compound&keys=%5B%5D&values=%5B%7B%22attributeId%22%3A%22compound_application_type_chebi%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2248318%22%7D%2C%7B%22categoryId%22%3A%2264857%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22compound_drug_indication_mesh_chembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22D009369%22%7D%2C%7B%22categoryId%22%3A%22D005261%22%7D%2C%7B%22categoryId%22%3A%22D002318%22%7D%2C%7B%22categoryId%22%3A%22D017437%22%7D%2C%7B%22categoryId%22%3A%22D013568%22%7D%2C%7B%22categoryId%22%3A%22D007239%22%7D%2C%7B%22categoryId%22%3A%22D006425%22%7D%2C%7B%22categoryId%22%3A%22D007154%22%7D%2C%7B%22categoryId%22%3A%22D009750%22%7D%2C%7B%22categoryId%22%3A%22D009358%22%7D%2C%7B%22categoryId%22%3A%22D009422%22%7D%2C%7B%22categoryId%22%3A%22D004066%22%7D%2C%7B%22categoryId%22%3A%22D004700%22%7D%2C%7B%22categoryId%22%3A%22D012140%22%7D%2C%7B%22categoryId%22%3A%22D064419%22%7D%2C%7B%22categoryId%22%3A%22D005128%22%7D%2C%7B%22categoryId%22%3A%22D014947%22%7D%2C%7B%22categoryId%22%3A%22D009140%22%7D%2C%7B%22categoryId%22%3A%22D009057%22%7D%2C%7B%22categoryId%22%3A%22D010038%22%7D%2C%7B%22categoryId%22%3A%22D052801%22%7D%2C%7B%22categoryId%22%3A%22D009784%22%7D%2C%7B%22categoryId%22%3A%22D000820%22%7D%5D%7D%5D)
    - Target: PubChem Compound（ChEMBL, ChEBIでも） 5件
    - もともとfragranceやcosmeticのAttributeを持つChEBI compoundが少ないので結果も少ない
- ▲とした懸念点(建石)
    - 結果が少ないのに例としていいのか

- [どう働くかよくわかっていないけれど薬効が認められている物質](https://togodx.dbcls.jp/human/?togoKey=mesh&keys=%5B%5D&values=%5B%7B%22attributeId%22%3A%22compound_application_type_chebi%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2252217%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22unclassified%22%7D%5D%7D%5D)
    - 504 Gateway Timeout
        - no chemble assayが74,473件なので多すぎる？
        - no chemble assayはタンパクを絞り込んでいる。pharmaceuticalは化合物を絞り込んでいる。重なっていないので数が減っていないのでは？
    - ChEMBL assay existenceがない、というので判断している
        - 薬効が認められているということはどこかでなんらかのassayが行われているはず。
    - ▲とした懸念点(建石)
        - assayがない= 働きがわかっていない としてしまっていいか
        - ChEMBL assay が存在する、ということは｢薬効に根拠がある?｣
    - [General Questions - ChEMBL Interface Documentation](https://chembl.gitbook.io/chembl-interface-documentation/frequently-asked-questions/general-questions)
- [biomarkerとしてアノテーションされている化合物が何の疾患に関係しているか](https://togodx-attribute-g3.dbcls.jp/human?togoKey=chebi&keys=%5B%7B%22attributeId%22%3A%22disease_diseases_mondo%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22compound_application_type_chebi%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2259163%22%2C%22ancestors%22%3A%5B%2247867%22%5D%7D%5D%7D%5D)
    - chebiのbiomarker 56件に対して、4つの化合物しか疾患と紐づかない
    - ▲とした懸念点(建石)
        - 結果が少ないのに例としていいのか

### Action type

- [疾患に対してinhibitorとして働く化合物をリストし、薬としての開発段階を確認する](https://togodx.dbcls.jp/human/?togoKey=mondo&keys=%5B%7B%22attributeId%22%3A%22compound_drug_development_phase_chembl%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22compound_action_type_chembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22INHIBITOR%22%7D%5D%7D%5D)
    - Target: Mondo 958件 （MeSH 1262、NANDO 0、HPO 122）
    - Action Type →INHIBITORでフィルターしたはずなのに、Map Attribute先のDrug Development Phaseではそれより多くの物質が表示されている
        - inhibitor-mondoのセット。ここで絞られたmondoに紐づいたchemicalになっているので。データとしては間違っていないのでは。
    - ▲とした懸念点(建石)
        - FilterされたものがMap Attribute先のIDへMapされるわけではないのでしょうか。だとするとFilterの結果残るものと残らないものがわかりやすい表示になっているとありがたいです。

### Biological role

- [inhibitorとして働く化合物をリストし、適応疾患にマップする](https://togodx.dbcls.jp/human/?togoKey=chembl_compound&keys=%5B%7B%22attributeId%22%3A%22compound_drug_indication_mesh_chembl%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22compound_biological_role_chebi%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2235222%22%7D%5D%7D%5D)
    - targetをchebi, pubchemにするとnullがたくさんでる
    - targetがChEMBLでもnullが出る、むしろChEBIだとnullはない (2/2。上の行はTypo？）
    - TargetがChEMBLのとき217件、ChEBIのとき318件、PubChemのとき298件

### Drug indication

- [薬効のある化粧品（香料含む）](https://togodx.dbcls.jp/human/?togoKey=pubchem_compound&keys=%5B%5D&values=%5B%7B%22attributeId%22%3A%22compound_application_type_chebi%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2248318%22%7D%2C%7B%22categoryId%22%3A%2264857%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22compound_drug_indication_mesh_chembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22D009369%22%7D%2C%7B%22categoryId%22%3A%22D005261%22%7D%2C%7B%22categoryId%22%3A%22D002318%22%7D%2C%7B%22categoryId%22%3A%22D017437%22%7D%2C%7B%22categoryId%22%3A%22D013568%22%7D%2C%7B%22categoryId%22%3A%22D007239%22%7D%2C%7B%22categoryId%22%3A%22D006425%22%7D%2C%7B%22categoryId%22%3A%22D007154%22%7D%2C%7B%22categoryId%22%3A%22D009750%22%7D%2C%7B%22categoryId%22%3A%22D009358%22%7D%2C%7B%22categoryId%22%3A%22D009422%22%7D%2C%7B%22categoryId%22%3A%22D004066%22%7D%2C%7B%22categoryId%22%3A%22D004700%22%7D%2C%7B%22categoryId%22%3A%22D012140%22%7D%2C%7B%22categoryId%22%3A%22D064419%22%7D%2C%7B%22categoryId%22%3A%22D005128%22%7D%2C%7B%22categoryId%22%3A%22D014947%22%7D%2C%7B%22categoryId%22%3A%22D009140%22%7D%2C%7B%22categoryId%22%3A%22D009057%22%7D%2C%7B%22categoryId%22%3A%22D010038%22%7D%2C%7B%22categoryId%22%3A%22D052801%22%7D%2C%7B%22categoryId%22%3A%22D009784%22%7D%2C%7B%22categoryId%22%3A%22D000820%22%7D%5D%7D%5D)
- [Infectionに効く薬の作用機序を見る](https://togodx.dbcls.jp/human/?togoKey=mesh&keys=%5B%7B%22attributeId%22%3A%22compound_action_type_chembl%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%221%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22compound_drug_indication_mesh_chembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22D007239%22%7D%5D%7D%5D)
    - TargetがMeSHで115件, Mondoで56件, HPOで5件, NANDOで0件
    - Drug indicationはchemblの中でmeshが記述されているものをとってきているはずだが、Targetの[MeshとDrug indicationが一致しない](https://togodx.dbcls.jp/human/?togoKey=chembl_compound&keys=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22compound_drug_indication_mesh_chembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22D009369%22%7D%2C%7B%22categoryId%22%3A%22D005261%22%7D%2C%7B%22categoryId%22%3A%22D002318%22%7D%2C%7B%22categoryId%22%3A%22D017437%22%7D%2C%7B%22categoryId%22%3A%22D000820%22%7D%2C%7B%22categoryId%22%3A%22D009784%22%7D%2C%7B%22categoryId%22%3A%22D052801%22%7D%2C%7B%22categoryId%22%3A%22D010038%22%7D%2C%7B%22categoryId%22%3A%22D009057%22%7D%2C%7B%22categoryId%22%3A%22D009140%22%7D%2C%7B%22categoryId%22%3A%22D014947%22%7D%2C%7B%22categoryId%22%3A%22D005128%22%7D%2C%7B%22categoryId%22%3A%22D064419%22%7D%2C%7B%22categoryId%22%3A%22D012140%22%7D%2C%7B%22categoryId%22%3A%22D004700%22%7D%2C%7B%22categoryId%22%3A%22D004066%22%7D%2C%7B%22categoryId%22%3A%22D009422%22%7D%2C%7B%22categoryId%22%3A%22D009358%22%7D%2C%7B%22categoryId%22%3A%22D009750%22%7D%2C%7B%22categoryId%22%3A%22D007154%22%7D%2C%7B%22categoryId%22%3A%22D006425%22%7D%2C%7B%22categoryId%22%3A%22D007239%22%7D%2C%7B%22categoryId%22%3A%22D013568%22%7D%5D%7D%5D)のはなぜ？→ 解決?sparqlist適用すればOKかも？
        - 守屋さんの[https://sparql-support.dbcls.jp/dxsk/build/](https://sparql-support.dbcls.jp/dxsk/build/)でみたが良いのかわからない
        - そもそもCHEMBL645にはsparqlでは「[D006470](http://identifiers.org/mesh/D006470)、[D002318](http://identifiers.org/mesh/D002318)、[D006973](http://identifiers.org/mesh/D006973)、[D003324](http://identifiers.org/mesh/D003324)、[D007863](http://identifiers.org/mesh/D007863)、[D065627](http://identifiers.org/mesh/D065627)」が返ってくるが[リンク](https://sparql-support.dbcls.jp/dxsk/build/?dataset=chembl_compound&annotations=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22compound_drug_indication_mesh_chembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D000820%22%7D%2C%7B%22node%22%3A%22D002318%22%7D%2C%7B%22node%22%3A%22D064419%22%7D%2C%7B%22node%22%3A%22D009358%22%7D%2C%7B%22node%22%3A%22D004066%22%7D%2C%7B%22node%22%3A%22D004700%22%7D%2C%7B%22node%22%3A%22D005128%22%7D%2C%7B%22node%22%3A%22D005261%22%7D%2C%7B%22node%22%3A%22D006425%22%7D%2C%7B%22node%22%3A%22D007154%22%7D%2C%7B%22node%22%3A%22D007239%22%7D%2C%7B%22node%22%3A%22D052801%22%7D%2C%7B%22node%22%3A%22D009140%22%7D%2C%7B%22node%22%3A%22D009369%22%7D%2C%7B%22node%22%3A%22D009422%22%7D%2C%7B%22node%22%3A%22D009750%22%7D%2C%7B%22node%22%3A%22D009784%22%7D%2C%7B%22node%22%3A%22D010038%22%7D%2C%7B%22node%22%3A%22D013568%22%7D%2C%7B%22node%22%3A%22D012140%22%7D%2C%7B%22node%22%3A%22D017437%22%7D%2C%7B%22node%22%3A%22D009057%22%7D%2C%7B%22node%22%3A%22D014947%22%7D%5D%7D%5D)でこれと一致しているのか定かでない。
    - Assayの有無とターゲットタンパク質にマップされますが、AssayのIDにマップできてもよいかもしれません（ChEMBL Assay ID へのマップを 作る必sparqlisttekiou 要がある）
        - ChEMBL Assay ID へのマップ：chembl_compound IDとChEMBL Assay IDを紐づけておく（TogoID）。Assayをtypeやcategory等で分類したバーを作成すればできるはず？

### Drug development phase

- [疾患に対してinhibitorとして働く化合物をリストし、薬としての開発段階を確認する](https://togodx.dbcls.jp/human/?togoKey=mondo&keys=%5B%7B%22attributeId%22%3A%22compound_drug_development_phase_chembl%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22compound_action_type_chembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22INHIBITOR%22%7D%5D%7D%5D)
    - リンクのクエリでは958件
    - リンクのクエリでは(ChEMBL) Action Type → INHIBITOR をフィルタとすることでInhibitorをとっているが、(CHEBI) Biological Role → Inhibitor にすると233件になる
        - この差はなぜ？
            - inhibitor と一概に言ってもchemblとchebiでinhibitorとしているセットが異なる
        - どちらが適切なのか？
            - 別のDBがそれぞれの基準でデータを作成しているのでなんとも言えないのでは。。

### PubChem ATC classification

- [Nutritional and metabolic diseasesに効く薬についてATC分類を見る](https://togodx.dbcls.jp/human/?togoKey=pubchem_compound&keys=%5B%7B%22attributeId%22%3A%22compound_atc_classification_pubchem%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22D009750%22%7D%5D%7D%5D)
    - ATCについてはPubChemとChEMBLで冗長ではないかとも思うが、どちらか一方でのみATCコードがついている物質があるので両方入れている。マージするのが良いのか？
    - [https://www.whocc.no/atc_ddd_index/?code=N06DX&showdescription=no](https://www.whocc.no/atc_ddd_index/?code=N06DX&showdescription=no)

### ChEMBL ATC classification

- [Nutritional and metabolic diseasesに効く薬についてATC分類を見る](https://togodx.dbcls.jp/human/?togoKey=chembl_compound&keys=%5B%7B%22attributeId%22%3A%22compound_atc_classification_chembl%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22D009750%22%7D%5D%7D%5D)
    - ↓からすると、どちらか一方にするならどちらかといえばChEMBLを残したほうがよさそう
- Nutritional and metabolic diseasesに効く薬についてATC ClassificationをPubChem,CheMBLの両方Map Attributeに指定してみた
    - ATCコードがChEMBLにはあるがPubChemにはない、というケースの方が多いように見えるがPubChemでついているもののセットがChEMBLでついているもののサブセットということはない
    - 生物学的には両方指定する意味はなさそう。同じ結果を出すはずのものを比較してみるということでデータクリーニングには役立つのでは?
    - [Targetが PubChemのとき](https://togodx.dbcls.jp/human/?togoKey=pubchem_compound&keys=%5B%7B%22attributeId%22%3A%22compound_atc_classification_pubchem%22%7D%2C%7B%22attributeId%22%3A%22compound_atc_classification_chembl%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22compound_drug_indication_mesh_chembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22D009750%22%7D%5D%7D%5D)888件、このときPubChemでATCがついていないとラベルがnull（詳細画面では表示される）
    - [TargetがChEMBLのとき](https://togodx.dbcls.jp/human/?togoKey=chembl_compound&keys=%5B%7B%22attributeId%22%3A%22compound_atc_classification_pubchem%22%7D%2C%7B%22attributeId%22%3A%22compound_atc_classification_chembl%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22compound_drug_indication_mesh_chembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22D009750%22%7D%5D%7D%5D)994件、ChEMBLでATCがついていなくてもラベルが表示される

↑　上記２つのATCのバーについて

・pubchemのATCのバーに紐づいている化合物：3380。

・chemblのATCのバーに紐づいている化合物：3400。

・(案として）KEGG MedicusがATCの情報とpubhcem, chemblへのリンクを持っているので、KEGG Medicusを使えば２つのバーの代替+αとなれる（ATCと紐づく化合物：5345。そのうちpubchemへのリンク：5321, chemblへのリンク：3730）。ライセンス：CC BY SA。ただRDFがないので作成が必要。

## Glycan

### Molecular mass of glycans

- [Target: ensembl gene / Filter: ChEBI epitope, Glycan mass 1200 - 1600Da / Map: Glycan Subsumption](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22glycan_subsumption_glycosmos%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22compound_biological_role_chebi%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2253000%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22glycan_mass_glycosmos%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%226%22%7D%2C%7B%22categoryId%22%3A%227%22%7D%5D%7D%5D)　（山本）
    - Filterでmassの幅を1200 - 1400 Da と 1400 - 1600 Da にしているにも関わらず、その他の重さも検索結果に表示されているのは何故だろう?
    - 関連リソース
        - [https://github.com/biosciencedbc/togosite-sparqlist/blob/main/repository/glycan_mass_glycosmos.md](https://github.com/biosciencedbc/togosite-sparqlist/blob/main/repository/glycan_mass_glycosmos.md)
        - [https://github.com/togodx/togodx-config-human/blob/develop/config/routing_org.json](https://github.com/togodx/togodx-config-human/blob/develop/config/routing_org.json)
- GlyCosmos
    - リンク切れ問題について確認する。→ 糖鎖チームに連絡済み。
        - [https://glycosmos.org/faq](https://glycosmos.org/faq) → [https://glycosmos.org/help](https://glycosmos.org/help) (これは要修正)
        - [https://glycosmos.org/glycans/show?gtc_id=G35609TJ](https://glycosmos.org/glycans/show?gtc_id=G35609TJ) → [https://glycosmos.org/glycans/show/G35609TJ](https://glycosmos.org/glycans/show/G35609TJ) (こちらは転送設定機能が追加される予定だが、ゆくゆくは改定後の表記方法に従うことが望ましい模様)

### Tissues

- [X染色体の遺伝子を、GlycanのTissuesにマップ](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22glycan_tissue_glycosmos%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2223%22%7D%5D%7D%5D)
    - colon, liver, heartが1件ずつ出てくる. (データをよく知らないと、解釈が難しい?)
    - ヒストグラムとテーブルで出てくるTissuesが合わない?

### Subsumption

- [epitopeとして機能する糖鎖がどれくらい詳しく分かっているか](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22glycan_subsumption_glycosmos%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22compound_biological_role_chebi%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2253000%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22glycan_mass_glycosmos%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%226%22%7D%2C%7B%22categoryId%22%3A%227%22%7D%5D%7D%5D)
    - もともとsubsumptionの意図は、抽象度を上げてあいまい検索をするためのもの
- [構造が分かっている糖鎖が、どのようなパスウェイのタンパク質を修飾するか](https://togodx.dbcls.jp/human/?togoKey=uniprot&keys=%5B%7B%22attributeId%22%3A%22interaction_proteins_in_pathway_reactome%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22glycan_subsumption_glycosmos%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%224%22%7D%5D%7D%5D)

## Disease

### Diseases in Mondo

- [miRNA遺伝子に関連する病気](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%5D&values=%5B%7B%22attributeId%22%3A%22gene_biotype_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22miRNA%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22disease_diseases_mondo%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%220003847%22%7D%5D%7D%5D)
    - 3つの遺伝子について、ENSGのリンクをクリックしていくと、確かに病気に関連する情報が見つかる.
    - Mondo にマップしたとき, ヒットの数が合わない? (ヒストグラムだと, Mendelian diseaseが2件だが, テーブルの中を見ると, Mendelian diseaseが3件?)
    - Select target datasetにNANDOを設定すると[結果](https://togodx.dbcls.jp/human/?togoKey=nando&keys=%5B%7B%22attributeId%22%3A%22disease_diseases_nando%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_biotype_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22miRNA%22%7D%5D%7D%5D)を取得できない？
        - NANDOとMONDOのリンクがないので，NANDOでは紐付けられてない
            - MONDO_0013114
            - MONDO_0013678
            - MONDO_0014747
            - MONDO_0032835
        - 上記のMONDOとNANDOに紐付きがないのを確認

### Diseases in MeSH

- [疾患に関与する環境汚染物質](https://togodx.dbcls.jp/human/?togoKey=chebi&keys=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22compound_chemical_role_chebi%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2278298%22%7D%5D%7D%5D)
- [環境汚染物質が薬として役立つ疾患](https://togodx.dbcls.jp/human/?togoKey=mesh&keys=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22compound_chemical_role_chebi%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2278298%22%7D%5D%7D%5D)
- [Chr15にある遺伝子に関連した病気](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2215%22%7D%5D%7D%5D)

### Diseases in NANDO

- [Y染色体にある遺伝子は、どのような難病に関連しているか](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22disease_diseases_nando%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2224%22%7D%5D%7D%5D)
    - Unclassifiedのみ
- [7番染色体にある遺伝子は、どのような難病に関連しているか](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22disease_diseases_nando%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2207%22%7D%5D%7D%5D)
    - エントリーのラベルではなく上位階層のラベルを表示するのはなぜか．
        - 階層を持つオントロジーの場合は，このような例が多い？
    - 日本語ラベルが存在する場合は，日本語ラベルを表示できないか．

### Cross referenced disease DBs in Mondo

- [ミトコンドリアゲノムの遺伝子から、疾患データベースへのリンク一覧](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22disease_related_dbs_mondo%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2225%22%7D%5D%7D%5D)
    - リンク種類の一覧が文字列ではなくリンクだと便利
        - 元々のデータがリンクではないので，現状では不可
        - filterとして使うと有用（結果からリンクとしては飛べないけど）

### Phenotypic abnormality

- [ミトコンドリアゲノムの遺伝子は、どのような異常形質に関連しているか](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22disease_phenotypic_abnormality_hpo%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2225%22%7D%5D%7D%5D)
    - 「遺伝子ー症状」の関連データはどこから取得しているか？
        - 例えば「MT-ATP6」遺伝子は，「Leber hereditary optic neuropathy」及び「NARP syndrome」の疾患原因遺伝子で，それら疾患に関連する症状は[10以上存在する](https://pubcasefinder.dbcls.jp/result?target=omim&phenotype=HP:0000347_ja,HP:0003022_ja,HP:0009381_ja,HP:0000204_ja,HP:0000625_ja&filter=GENEID:4508&size=10&display_format=full&lang=ja)．
            - PubCaseFinderのRDFを使えば可能
                - PubCaseFinderにIDがない問題で保留されていたが，IDを付けたので今のバージョンならできるかも？（シンさんに確認）
        - しかし，TogoDX上で「MT-ATP6」遺伝子に関連する症状はHP:0001112の「Leber optic atrophy」のみ
    - モーダルのHPO内容表示
        - 大見出しのIDのprefix: HPO -> HP
            - メタスタンザ修正済 (池田さん)

## Variant

### GWAS

- [GWASでアルツハイマー病に関連付けられたタンパク質のαヘリックス数](https://togodx.dbcls.jp/human/?togoKey=uniprot&keys=%5B%7B%22attributeId%22%3A%22structure_number_of_alpha_helices_pdb%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22variant_gwas_togovar%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22EFO_0009268%22%2C%22ancestors%22%3A%5B%22IAO_0000030%22%2C%22EFO_0000352%22%2C%22EFO_0000493%22%5D%7D%5D%7D%5D)
    - 12と32にピークがある → 解釈は可能か?

### Clinical significance

- [病原性を持つバリアントを持つ遺伝子が、どの染色体にあるか](https://togodx.dbcls.jp/human/?togoKey=ensembl_gene&keys=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22variant_clinical_significance_togovar%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22pathogenic_or_likely_pathogenic%22%7D%5D%7D%5D)
    - Pathogenic/Likely pathogenicに限定. Pathogenicにすると時間がかかる?
- [病原性を持つバリアントが、どのような病気に関連しているか](https://togodx.dbcls.jp/human/?togoKey=mondo&keys=%5B%7B%22attributeId%22%3A%22disease_diseases_mondo%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22variant_clinical_significance_togovar%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%22pathogenic_or_likely_pathogenic%22%7D%5D%7D%5D)

