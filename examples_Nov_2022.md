# TogoDX/Human 検索事例集(2022年11月)

## Gene
### Gene biotype

- [miRNAに原因のある遺伝性疾患](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%5D&filters=%5B%7B%22attributeId%22%3A%22gene_biotype_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22miRNA%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22disease_diseases_mondo%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%220003847%22%7D%5D%7D%5D) 
    - MIR96, MIR140, MIR204 (難聴, 脊椎骨端異形成症, 網膜ジストロフィー)
        - MIR96 ENSG00000199158 Autosomal dominant non-syndromic sensorineural deafness type DFNA
        - MIR140 ENSG00000208017 Spondyloepiphyseal dysplasia, Nishimura type
        - MIR204 ENSG00000207935 Familial progressive retinal dystrophy-iris coloboma-congenital cataract syndrome

### Chromosome

- [Y染色体の遺伝子が特異的に発現している組織を見る](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22gene_high_level_expression_refex%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2224%22%7D%5D%7D%5D) 
    - Testis特異的発現が多い

- [Y染色体の遺伝子は、どのような病気に関連しているか](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2224%22%7D%5D%7D%5D)
    - 1件ヒット: SRY遺伝子 (sex determining region Y)
- [神経系疾患に関連する遺伝子が、どの染色体にあるか](https://togodx.dbcls.jp/human/?dataset=mesh&annotations=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D009422%22%7D%5D%7D%5D)
- [MTゲノムにコードされているタンパク質は、構造が決まっているか](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22structure_data_existence_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2225%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22gene_biotype_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22protein_coding%22%7D%5D%7D%5D) 
    - 構造が決まっているものが比較的多い. 決まっていないものが2つあるが (MT-ATP6, MT-ATP8) , この2つも重要なものらしい. ([link](http://grj.umin.jp/grj/mt-overview.htm)).


### # of paralogs

- [singletonをターゲットとしてmetabolic diseasesに効く薬](https://togodx.dbcls.jp/human/?dataset=chebi&annotations=%5B%5D&filters=%5B%7B%22attributeId%22%3A%22gene_number_of_paralogs_homologene%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22paralog_count_01%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22disease_diseases_mesh%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D008659%22%2C%22ancestors%22%3A%5B%22D009750%22%5D%7D%5D%7D%5D)

### Ortholog existence
- [小脳特異的に発現している遺伝子のオーソログはどのような生物で見つかるか](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22gene_ortholog_existence_homologene%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_high_level_expression_refex%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22v02_40%22%7D%5D%7D%5D)

### Evolutionary divergence

- [zinc-fingerドメイン持ち、そのオルソログがマウスやラットにあるタンパク質をターゲットとする薬](https://togodx.dbcls.jp/human/?dataset=chebi&annotations=%5B%5D&filters=%5B%7B%22attributeId%22%3A%22gene_evolutionary_conservation_homologene%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22branch_04%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22protein_domains_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22863%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D)

### Biological process

### Cellular component

### Molecular function

### Tissue-specific high expression (RefEx GeneChip)

- [環境汚染物質がターゲットとする遺伝子がどこで高発現しているか](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22gene_high_level_expression_refex%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22compound_chemical_role_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2278298%22%7D%5D%7D%5D)

### Tissue-specific low expression (RefEx GeneChip)

- [Y染色体の遺伝子の発現特異性](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22gene_low_level_expression_refex%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2224%22%7D%5D%7D%5D)

### Tissue-specific high expression (GTEx)

- [Y染色体の遺伝子の発現特異性](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22gene_not_expressed_in_tissues_gtex%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2224%22%7D%5D%7D%5D)

### No expression in tissues (GTEx)

- [Y染色体の遺伝子の発現特異性](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22gene_specific_expression_in_tissues_hpa%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2224%22%7D%5D%7D%5D)

### Tissue-specific high expression (HPA)

- [Y染色体の遺伝子の発現特異性](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22gene_specific_expression_in_tissues_hpa%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2224%22%7D%5D%7D%5D)

### Cell type-specific high expression (HPA)

- [Y染色体の遺伝子の発現特異性](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22gene_specific_expression_in_cells_hpa%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2224%22%7D%5D%7D%5D)

### Transcript biotype

### Transcript length

## Protein

### UniProtKB sections

### Protein domains

- [免疫グロブリンドメインを持つタンパク質をコードする遺伝子のGO(Biological process)一覧](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22protein_biological_process_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22protein_domains_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22393%22%7D%5D%7D%5D)

### Cellular component

- [ミトコンドリアゲノムにコードされたタンパク質の細胞内局在](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22protein_cellular_component_uniprot%22%2C%22id%22%3A%7B%22node%22%3A%22GO_0110165%22%2C%22ancestors%22%3A%5B%5D%7D%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2225%22%7D%5D%7D%5D)

### Biological process

- [免疫グロブリンドメインを持つタンパク質をコードする遺伝子のGO(Biological process)一覧](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22protein_biological_process_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22protein_domains_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22393%22%7D%5D%7D%5D)

### Molecular function

- [ミトコンドリアゲノムにコードされた遺伝子のGO(Molecular function)](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22protein_molecular_function_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2225%22%7D%5D%7D%5D)

### Isoform specific GO existence

### Ligands

- [DNA結合型転写因子として組織特異的に高発現し、Zincと結合･反応して機能するタンパク質の一覧](https://togodx.dbcls.jp/human/?dataset=uniprot&annotations=%5B%7B%22attributeId%22%3A%22gene_high_level_expression_refex%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22protein_molecular_function_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22GO_0003700%22%2C%22ancestors%22%3A%5B%22GO_0140110%22%5D%7D%5D%7D%2C%7B%22attributeId%22%3A%22protein_ligands_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22862%22%7D%5D%7D%5D)　

### Molecular mass

- [分子量が100kDa以上でDNA結合型転写因子として組織特異的に高発現し、Zincと結合･反応して機能するタンパク質の一覧](https://togodx.dbcls.jp/human/?dataset=uniprot&annotations=%5B%7B%22attributeId%22%3A%22gene_high_level_expression_refex%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22protein_molecular_function_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22GO_0003700%22%2C%22ancestors%22%3A%5B%22GO_0140110%22%5D%7D%5D%7D%2C%7B%22attributeId%22%3A%22protein_molecular_mass_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2211%22%7D%2C%7B%22node%22%3A%2212%22%7D%2C%7B%22node%22%3A%2213%22%7D%2C%7B%22node%22%3A%2214%22%7D%2C%7B%22node%22%3A%2215%22%7D%2C%7B%22node%22%3A%2216%22%7D%2C%7B%22node%22%3A%2217%22%7D%2C%7B%22node%22%3A%2218%22%7D%2C%7B%22node%22%3A%2219%22%7D%2C%7B%22node%22%3A%2220%22%7D%2C%7B%22node%22%3A%2221%22%7D%2C%7B%22node%22%3A%2222%22%7D%2C%7B%22node%22%3A%2223%22%7D%2C%7B%22node%22%3A%2224%22%7D%2C%7B%22node%22%3A%2225%22%7D%2C%7B%22node%22%3A%2226%22%7D%2C%7B%22node%22%3A%2227%22%7D%2C%7B%22node%22%3A%2228%22%7D%2C%7B%22node%22%3A%2229%22%7D%2C%7B%22node%22%3A%2230%22%7D%2C%7B%22node%22%3A%2231%22%7D%2C%7B%22node%22%3A%2232%22%7D%2C%7B%22node%22%3A%2233%22%7D%2C%7B%22node%22%3A%2234%22%7D%2C%7B%22node%22%3A%2235%22%7D%2C%7B%22node%22%3A%2236%22%7D%2C%7B%22node%22%3A%2237%22%7D%2C%7B%22node%22%3A%2238%22%7D%2C%7B%22node%22%3A%2239%22%7D%2C%7B%22node%22%3A%2240%22%7D%2C%7B%22node%22%3A%2241%22%7D%2C%7B%22node%22%3A%2242%22%7D%2C%7B%22node%22%3A%2243%22%7D%2C%7B%22node%22%3A%2244%22%7D%2C%7B%22node%22%3A%2245%22%7D%2C%7B%22node%22%3A%2246%22%7D%2C%7B%22node%22%3A%2247%22%7D%2C%7B%22node%22%3A%2248%22%7D%2C%7B%22node%22%3A%2249%22%7D%2C%7B%22node%22%3A%2250%22%7D%2C%7B%22node%22%3A%2251%22%7D%2C%7B%22node%22%3A%2252%22%7D%2C%7B%22node%22%3A%2253%22%7D%2C%7B%22node%22%3A%2254%22%7D%2C%7B%22node%22%3A%2255%22%7D%2C%7B%22node%22%3A%2256%22%7D%2C%7B%22node%22%3A%2257%22%7D%2C%7B%22node%22%3A%2258%22%7D%2C%7B%22node%22%3A%2259%22%7D%2C%7B%22node%22%3A%2260%22%7D%2C%7B%22node%22%3A%2262%22%7D%2C%7B%22node%22%3A%2263%22%7D%2C%7B%22node%22%3A%2264%22%7D%2C%7B%22node%22%3A%2265%22%7D%2C%7B%22node%22%3A%2270%22%7D%2C%7B%22node%22%3A%2273%22%7D%2C%7B%22node%22%3A%2274%22%7D%2C%7B%22node%22%3A%2278%22%7D%2C%7B%22node%22%3A%2279%22%7D%2C%7B%22node%22%3A%2280%22%7D%2C%7B%22node%22%3A%2281%22%7D%2C%7B%22node%22%3A%2284%22%7D%2C%7B%22node%22%3A%2285%22%7D%2C%7B%22node%22%3A%2286%22%7D%2C%7B%22node%22%3A%2287%22%7D%2C%7B%22node%22%3A%2289%22%7D%2C%7B%22node%22%3A%2297%22%7D%2C%7B%22node%22%3A%2298%22%7D%2C%7B%22node%22%3A%22101%22%7D%2C%7B%22node%22%3A%22102%22%7D%2C%7B%22node%22%3A%22152%22%7D%2C%7B%22node%22%3A%22302%22%7D%2C%7B%22node%22%3A%22382%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22protein_ligands_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22862%22%7D%5D%7D%5D)　


### PTMs

- [Viral processに関わり、Glycoprotein(糖タンパク質)の翻訳後修飾を受けるタンパク質のうち、組織別に結合する糖鎖の種類が明らかになっているかを調べる(かつ、それらの遺伝子の組織における発現状況を調べる)。](https://togodx.dbcls.jp/human/?dataset=uniprot&annotations=%5B%7B%22attributeId%22%3A%22glycan_tissue_glycosmos%22%7D%2C%7B%22attributeId%22%3A%22gene_high_level_expression_refex%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22protein_ptms_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22325%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22protein_biological_process_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22GO_0016032%22%7D%5D%7D%5D)　

### Catalytic activity

### # of transmembrane domains

- [Gタンパク質共役型ペプチドレセプタータンパク質の膜貫通型ドメインの数とそれらの立体構造データの有無](https://togodx.dbcls.jp/human/?dataset=uniprot&annotations=%5B%7B%22attributeId%22%3A%22protein_number_of_transmembrane_domains_uniprot%22%7D%2C%7B%22attributeId%22%3A%22structure_data_existence_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22protein_molecular_function_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22GO_0008528%22%2C%22ancestors%22%3A%5B%22GO_0060089%22%2C%22GO_0038023%22%2C%22GO_0004888%22%2C%22GO_0004930%22%5D%7D%5D%7D%5D)　

### # of phosphorylation sites

- [タンパク質ポリンについて、リン酸化部位の数、膜貫通型ドメインの数、および局在を見る](https://togodx.dbcls.jp/human/?dataset=uniprot&annotations=%5B%7B%22attributeId%22%3A%22protein_number_of_transmembrane_domains_uniprot%22%7D%2C%7B%22attributeId%22%3A%22protein_number_of_phosphorylation_sites_uniprot%22%7D%2C%7B%22attributeId%22%3A%22protein_cellular_component_uniprot%22%2C%22id%22%3A%7B%22node%22%3A%22GO_0016020%22%2C%22ancestors%22%3A%5B%22GO_0110165%22%5D%7D%7D%5D&filters=%5B%7B%22attributeId%22%3A%22protein_domains_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22626%22%2C%22ancestors%22%3A%5B%22812%22%5D%7D%5D%7D%5D) 

### # of glycosylation sites

- [免疫グロブリンドメインを持つタンパク質について、糖鎖修飾部位の数、リン酸化部位の数、膜貫通型ドメインの数を見る](https://togodx.dbcls.jp/human/?dataset=uniprot&annotations=%5B%7B%22attributeId%22%3A%22protein_number_of_glycosylation_sites_uniprot%22%7D%2C%7B%22attributeId%22%3A%22protein_number_of_phosphorylation_sites_uniprot%22%7D%2C%7B%22attributeId%22%3A%22protein_number_of_transmembrane_domains_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22protein_domains_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22393%22%7D%5D%7D%5D) 


### Disease-related proteins

- [Y染色体にある遺伝子は、どのような病気に関連しているか](https://togodx.dbcls.jp/human/?dataset=uniprot&annotations=%5B%7B%22attributeId%22%3A%22protein_disease_related_proteins_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2224%22%7D%5D%7D%5D)

### Tissues w/expression reported

- [Y染色体の遺伝子の発現特異性](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22protein_isolation_source_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2224%22%7D%5D%7D%5D)

### Evidence of existence

- [ホモロジーから存在が推測されるタンパク質は、どの染色体にコードされていて、どんなドメインを持っているか](https://togodx.dbcls.jp/human/?dataset=uniprot&annotations=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%7D%2C%7B%22attributeId%22%3A%22protein_domains_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22protein_evidence_of_existence_nextprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%223%22%7D%5D%7D%5D) (UniProt 147件)
    - 11番染色体に多く、膜貫通型ドメインが多い

### Isoform specific interaction existence

### Pathway annotation

## Structure

### Structure data existence
- [構造を持つタンパク質と遺伝子の染色体ごとの分布](https://togodx.dbcls.jp/human/?dataset=pdb&annotations=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22structure_data_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D)

- [疾患に関連する構造タンパク質と遺伝子の染色体ごとの分布](https://togodx.dbcls.jp/human/?dataset=mondo&annotations=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22structure_data_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D)

### Rate of helical regions
- [Cell projection membrane に関わるタンパク質(UniProt)におけるHelical regionの割合の分布](https://togodx.dbcls.jp/human/?dataset=uniprot&annotations=%5B%7B%22attributeId%22%3A%22structure_helical_regions_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22protein_cellular_component_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22GO_0097060%22%2C%22ancestors%22%3A%5B%22GO_0110165%22%2C%22GO_0016020%22%2C%22GO_0098590%22%5D%7D%5D%7D%5D)

- [Synaptic membrane に関わるタンパク質(UniProt)におけるHelical regionの割合の分布](https://togodx.dbcls.jp/human/?dataset=uniprot&annotations=%5B%7B%22attributeId%22%3A%22structure_helical_regions_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22protein_cellular_component_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22GO_0097060%22%2C%22ancestors%22%3A%5B%22GO_0110165%22%2C%22GO_0016020%22%2C%22GO_0098590%22%5D%7D%5D%7D%5D)
    - Synaptic membraneと比べると、Cell projection membrane ではHelical regionの割合が高い(50%以上)タンパク質が、多く含まれていることがわかる。

### Rate of beta strand
- [Cell projection membrane に関わるタンパク質(UniProt)におけるBeta strandの割合の分布](https://togodx.dbcls.jp/human/?dataset=uniprot&annotations=%5B%7B%22attributeId%22%3A%22structure_beta_strand_regions_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22protein_cellular_component_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22GO_0031253%22%2C%22ancestors%22%3A%5B%22GO_0110165%22%2C%22GO_0016020%22%2C%22GO_0098590%22%5D%7D%5D%7D%5D)

- [Synaptic membrane に関わるタンパク質(UniProt)におけるBeta strandの割合の分布](https://togodx.dbcls.jp/human/?dataset=uniprot&annotations=%5B%7B%22attributeId%22%3A%22structure_helical_regions_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22protein_cellular_component_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22GO_0097060%22%2C%22ancestors%22%3A%5B%22GO_0110165%22%2C%22GO_0016020%22%2C%22GO_0098590%22%5D%7D%5D%7D%5D)
    - Beta strand では、Synaptic membraneとCell projection membrane を比べて大きな差はないことがわかる。

### # of turn structures

### # of disulfide bonds

### Rate of disorder regions

### # of peptides in a PDB entry

- [Y染色体上の遺伝子がコードするタンパク質が持つペプチドの数](https://togodx.dbcls.jp/human/?dataset=uniprot&annotations=%5B%7B%22attributeId%22%3A%22structure_number_of_peptides_pdb%22%7D%2C%7B%22attributeId%22%3A%22structure_data_existence_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2224%22%7D%5D%7D%5D)
    - ペプチドの数は、実験手法的に前例のあるダイマーや複合体などを形成していそうだということがわかる

### Analysis methods

- [Neutron diffraction(中性子回折法)を使って同定したPDBエントリに関連する疾患と遺伝子の染色体ごとの分布](https://togodx.dbcls.jp/human/?dataset=nando&annotations=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22structure_analysis_methods_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2204%22%7D%5D%7D%5D)

## Interaction

### Proteins in pathway

- [目的の反応にcomponentとして参加する化合物とタンパク質をリストし、そのタンパク質の構造が解析されているかどうかを調べる](https://togodx.dbcls.jp/human/?dataset=chebi&annotations=%5B%7B%22attributeId%22%3A%22structure_data_existence_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22interaction_proteins_in_pathway_reactome%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22R-HSA-2162123%22%2C%22ancestors%22%3A%5B%22R-HSA-1430728%22%2C%22R-HSA-556833%22%2C%22R-HSA-8978868%22%2C%22R-HSA-2142753%22%5D%7D%5D%7D%2C%7B%22attributeId%22%3A%22interaction_compounds_in_pathway_reactome%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22R-HSA-2162123%22%2C%22ancestors%22%3A%5B%22R-HSA-1430728%22%2C%22R-HSA-556833%22%2C%22R-HSA-8978868%22%2C%22R-HSA-2142753%22%5D%7D%5D%7D%5D)

### Compounds in pathway

- [目的の反応にcomponentとして参加する化合物とタンパク質をリストし、そのタンパク質の構造が解析されているかどうかを調べる](https://togodx.dbcls.jp/human/?dataset=chebi&annotations=%5B%7B%22attributeId%22%3A%22structure_data_existence_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22interaction_proteins_in_pathway_reactome%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22R-HSA-2162123%22%2C%22ancestors%22%3A%5B%22R-HSA-1430728%22%2C%22R-HSA-556833%22%2C%22R-HSA-8978868%22%2C%22R-HSA-2142753%22%5D%7D%5D%7D%2C%7B%22attributeId%22%3A%22interaction_compounds_in_pathway_reactome%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22R-HSA-2162123%22%2C%22ancestors%22%3A%5B%22R-HSA-1430728%22%2C%22R-HSA-556833%22%2C%22R-HSA-8978868%22%2C%22R-HSA-2142753%22%5D%7D%5D%7D%5D)

### # of interacting proteins

- [Infectionsに関わる化合物が相互作用するタンパク質の数を知りたい](https://togodx.dbcls.jp/human/?dataset=chembl_compound&annotations=%5B%7B%22attributeId%22%3A%22interaction_number_of_interacting_proteins_uniprot%22%7D%2C%7B%22attributeId%22%3A%22interaction_chembl_assay_existence_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D007239%22%7D%5D%7D%5D)

### ChEMBL assay existence

- [ミトコンドリアゲノム由来のタンパク質をターゲットとする薬とその適用疾患](https://togodx.dbcls.jp/human/?dataset=chebi&annotations=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2225%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D)

- [どう働くかよくわかっていないけれど薬効が認められている物質](https://togodx.dbcls.jp/human/?dataset=mesh&annotations=%5B%5D&filters=%5B%7B%22attributeId%22%3A%22compound_application_type_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2252217%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22unclassified%22%7D%5D%7D%5D)

## Compound


### Chemical role

- [環境汚染物質がターゲットとする遺伝子がどこで高発現しているか](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22gene_high_level_expression_refex%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22compound_chemical_role_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2278298%22%7D%5D%7D%5D)

- [疾患に関与する環境汚染物質](https://togodx.dbcls.jp/human/?dataset=chebi&annotations=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22compound_chemical_role_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2278298%22%7D%5D%7D%5D)
    - Chemical CompoundとDiseases in MeSHはChEMBL Drug Indicationを通してつながっているはずなので、疾患に薬効を持つ環境汚染物質という意味になると思われるが、それがわかりにくい


### Application type

- [薬効のある化粧品（香料含む）](https://togodx.dbcls.jp/human/?dataset=pubchem_compound&annotations=%5B%5D&filters=%5B%7B%22attributeId%22%3A%22compound_application_type_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2248318%22%7D%2C%7B%22node%22%3A%2264857%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22compound_drug_indication_mesh_chembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D009369%22%7D%2C%7B%22node%22%3A%22D005261%22%7D%2C%7B%22node%22%3A%22D002318%22%7D%2C%7B%22node%22%3A%22D017437%22%7D%2C%7B%22node%22%3A%22D013568%22%7D%2C%7B%22node%22%3A%22D007239%22%7D%2C%7B%22node%22%3A%22D006425%22%7D%2C%7B%22node%22%3A%22D007154%22%7D%2C%7B%22node%22%3A%22D009750%22%7D%2C%7B%22node%22%3A%22D009358%22%7D%2C%7B%22node%22%3A%22D009422%22%7D%2C%7B%22node%22%3A%22D004066%22%7D%2C%7B%22node%22%3A%22D004700%22%7D%2C%7B%22node%22%3A%22D012140%22%7D%2C%7B%22node%22%3A%22D064419%22%7D%2C%7B%22node%22%3A%22D005128%22%7D%2C%7B%22node%22%3A%22D014947%22%7D%2C%7B%22node%22%3A%22D009140%22%7D%2C%7B%22node%22%3A%22D009057%22%7D%2C%7B%22node%22%3A%22D010038%22%7D%2C%7B%22node%22%3A%22D052801%22%7D%2C%7B%22node%22%3A%22D009784%22%7D%2C%7B%22node%22%3A%22D000820%22%7D%5D%7D%5D)


- [どう働くかよくわかっていないけれど薬効が認められている物質](https://togodx.dbcls.jp/human/?dataset=mesh&annotations=%5B%5D&filters=%5B%7B%22attributeId%22%3A%22compound_application_type_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2252217%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22unclassified%22%7D%5D%7D%5D)
    - assayがない ≒ 働きがわかっていない
    - ChEMBL assay が存在する ≒ 薬効に根拠がある

- [biomarkerとしてアノテーションされている化合物が何の疾患に関係しているか](https://togodx.dbcls.jp/human/?dataset=chebi&annotations=%5B%7B%22attributeId%22%3A%22disease_diseases_mondo%22%7D%5D&values=%5B%7B%22attributeId%22%3A%22compound_application_type_chebi%22%2C%22ids%22%3A%5B%7B%22categoryId%22%3A%2259163%22%2C%22ancestors%22%3A%5B%2247867%22%5D%7D%5D%7D%5D)


### Action type

- [疾患に対してinhibitorとして働く化合物をリストし、薬としての開発段階を確認する](https://togodx.dbcls.jp/human/?dataset=mondo&annotations=%5B%7B%22attributeId%22%3A%22compound_drug_development_phase_chembl%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22compound_action_type_chembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22INHIBITOR%22%7D%5D%7D%5D)



### Biological role

- [inhibitorとして働く化合物をリストし、適応疾患にマップする](https://togodx.dbcls.jp/human/?dataset=chembl_compound&annotations=%5B%7B%22attributeId%22%3A%22compound_drug_indication_mesh_chembl%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22compound_biological_role_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2235222%22%7D%5D%7D%5D)


### Drug indication

- [薬効のある化粧品（香料含む）](https://togodx.dbcls.jp/human/?dataset=pubchem_compound&annotations=%5B%5D&filters=%5B%7B%22attributeId%22%3A%22compound_application_type_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2248318%22%7D%2C%7B%22node%22%3A%2264857%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22compound_drug_indication_mesh_chembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D009369%22%7D%2C%7B%22node%22%3A%22D005261%22%7D%2C%7B%22node%22%3A%22D002318%22%7D%2C%7B%22node%22%3A%22D017437%22%7D%2C%7B%22node%22%3A%22D013568%22%7D%2C%7B%22node%22%3A%22D007239%22%7D%2C%7B%22node%22%3A%22D006425%22%7D%2C%7B%22node%22%3A%22D007154%22%7D%2C%7B%22node%22%3A%22D009750%22%7D%2C%7B%22node%22%3A%22D009358%22%7D%2C%7B%22node%22%3A%22D009422%22%7D%2C%7B%22node%22%3A%22D004066%22%7D%2C%7B%22node%22%3A%22D004700%22%7D%2C%7B%22node%22%3A%22D012140%22%7D%2C%7B%22node%22%3A%22D064419%22%7D%2C%7B%22node%22%3A%22D005128%22%7D%2C%7B%22node%22%3A%22D014947%22%7D%2C%7B%22node%22%3A%22D009140%22%7D%2C%7B%22node%22%3A%22D009057%22%7D%2C%7B%22node%22%3A%22D010038%22%7D%2C%7B%22node%22%3A%22D052801%22%7D%2C%7B%22node%22%3A%22D009784%22%7D%2C%7B%22node%22%3A%22D000820%22%7D%5D%7D%5D)
- [Infectionに効く薬の作用機序を見る](https://togodx.dbcls.jp/human/?dataset=mesh&annotations=%5B%7B%22attributeId%22%3A%22compound_action_type_chembl%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22compound_drug_indication_mesh_chembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D007239%22%7D%5D%7D%5D)
 


### Drug development phase

- [疾患に対してinhibitorとして働く化合物をリストし、薬としての開発段階を確認する](https://togodx.dbcls.jp/human/?dataset=mondo&annotations=%5B%7B%22attributeId%22%3A%22compound_drug_development_phase_chembl%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22compound_action_type_chembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22INHIBITOR%22%7D%5D%7D%5D)
 

### PubChem ATC classification

- [Nutritional and metabolic diseasesに効く薬についてATC分類を見る](https://togodx.dbcls.jp/human/?dataset=pubchem_compound&annotations=%5B%7B%22attributeId%22%3A%22compound_atc_classification_pubchem%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D009750%22%7D%5D%7D%5D)


### ChEMBL ATC classification

- [Nutritional and metabolic diseasesに効く薬についてATC分類を見る](https://togodx.dbcls.jp/human/?dataset=chembl_compound&annotations=%5B%7B%22attributeId%22%3A%22compound_atc_classification_chembl%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D009750%22%7D%5D%7D%5D)


## Glycan

### Molecular mass of glycans

- [Target: ensembl gene / Filter: ChEBI epitope, Glycan mass 1200 - 1600Da / Map: Glycan Subsumption](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22glycan_subsumption_glycosmos%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22compound_biological_role_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2253000%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22glycan_mass_glycosmos%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%226%22%7D%2C%7B%22node%22%3A%227%22%7D%5D%7D%5D)　



### Tissues

- [X染色体の遺伝子を、GlycanのTissuesにマップ](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22glycan_tissue_glycosmos%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2223%22%7D%5D%7D%5D)


### Subsumption

- [epitopeとして機能する糖鎖がどれくらい詳しく分かっているか](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22glycan_subsumption_glycosmos%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22compound_biological_role_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2253000%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22glycan_mass_glycosmos%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%226%22%7D%2C%7B%22node%22%3A%227%22%7D%5D%7D%5D)
    - もともとsubsumptionの意図は、抽象度を上げてあいまい検索をするためのもの
- [構造が分かっている糖鎖が、どのようなパスウェイのタンパク質を修飾するか](https://togodx.dbcls.jp/human/?dataset=uniprot&annotations=%5B%7B%22attributeId%22%3A%22interaction_proteins_in_pathway_reactome%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22glycan_subsumption_glycosmos%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%224%22%7D%5D%7D%5D)

## Disease

### Diseases in Mondo

- [miRNA遺伝子に関連する病気](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%5D&filters=%5B%7B%22attributeId%22%3A%22gene_biotype_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22miRNA%22%7D%5D%7D%2C%7B%22attributeId%22%3A%22disease_diseases_mondo%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%220003847%22%7D%5D%7D%5D)

    - [Diseases in Mondo に Map attribute した場合](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22disease_diseases_mondo%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_biotype_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22miRNA%22%7D%5D%7D%5D)

### Diseases in MeSH

- [疾患に関与する環境汚染物質](https://togodx.dbcls.jp/human/?dataset=chebi&annotations=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22compound_chemical_role_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2278298%22%7D%5D%7D%5D)
- [環境汚染物質が薬として役立つ疾患](https://togodx.dbcls.jp/human/?dataset=mesh&annotations=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22compound_chemical_role_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2278298%22%7D%5D%7D%5D)
- [Chr15にある遺伝子に関連した病気](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22disease_diseases_mesh%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2215%22%7D%5D%7D%5D)

### Diseases in NANDO

- [Y染色体にある遺伝子は、どのような難病に関連しているか](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22disease_diseases_nando%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2224%22%7D%5D%7D%5D)
    - Unclassifiedのみ
- [7番染色体にある遺伝子は、どのような難病に関連しているか](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22disease_diseases_nando%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2207%22%7D%5D%7D%5D)


### Cross referenced disease DBs in Mondo

- [ミトコンドリアゲノムの遺伝子から、疾患データベースへのリンク一覧](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22disease_related_dbs_mondo%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2225%22%7D%5D%7D%5D)


### Phenotypic abnormality

- [ミトコンドリアゲノムの遺伝子は、どのような異常形質に関連しているか](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22disease_phenotypic_abnormality_hpo%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2225%22%7D%5D%7D%5D)

## Variant
### GWAS

- [GWASでアルツハイマー病に関連付けられたタンパク質(UniProt)におけるHelical regionの割合の分布](https://togodx.dbcls.jp/human/?dataset=uniprot&annotations=%5B%7B%22attributeId%22%3A%22structure_helical_regions_uniprot%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22variant_gwas_togovar%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22EFO_0009268%22%2C%22ancestors%22%3A%5B%22IAO_0000030%22%2C%22EFO_0000352%22%2C%22EFO_0000493%22%5D%7D%5D%7D%5D)

### Clinical significance

- [病原性を持つバリアントを持つ遺伝子が、どの染色体にあるか](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attributeId%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22variant_clinical_significance_togovar%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22pathogenic_or_likely_pathogenic%22%7D%5D%7D%5D)
    - Pathogenic/Likely pathogenicに限定. 

- [病原性を持つバリアントが、どのような病気に関連しているか](https://togodx.dbcls.jp/human/?dataset=mondo&annotations=%5B%7B%22attributeId%22%3A%22disease_diseases_mondo%22%7D%5D&filters=%5B%7B%22attributeId%22%3A%22variant_clinical_significance_togovar%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22pathogenic_or_likely_pathogenic%22%7D%5D%7D%5D)

