import requests
"""
This takes in an arxiv link and outputs a bibtex.
"""


# TODO(Adriano) we will use this 
# import pydantic
# class Bibtex(pydantic.BaseModel):
#     # Example:
#     # @misc{betley2025emergentmisalignmentnarrowfinetuning,
#     #     title={Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs}, 
#     #     author={Jan Betley and Daniel Tan and Niels Warncke and Anna Sztyber-Betley and Xuchan Bao and Martín Soto and Nathan Labenz and Owain Evans},
#     #     year={2025},
#     #     eprint={2502.17424},
#     #     archivePrefix={arXiv},
#     #     primaryClass={cs.CL},
#     #     url={https://arxiv.org/abs/2502.17424}, 
#     # }
#     title: str
#     author: str
#     year: int
#     eprint: str
#     archivePrefix: str = "arXiv"
#     primaryClass: str = "cs.CL"
#     url: str

title = "Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs"
author = "Jan Betley and Daniel Tan and Niels Warncke and Anna Sztyber-Betley and Xuchan Bao and Martín Soto and Nathan Labenz and Owain Evans"
year = "2025"
eprint = "2502.17424"
archivePrefix = "arXiv"
primaryClass = "cs.CL"
url = "https://arxiv.org/abs/2502.17424"

example = "https://arxiv.org/abs/2502.17424"
content = requests.get(example)

# print(content.text)
# print("title in content=", title in content.text)
# print("author in content=", author in content.text)
# print("year in content=", year in content.text)
# print("eprint in content=", eprint in content.text)
# print("archivePrefix in content=", archivePrefix in content.text)
# print("primaryClass in content=", primaryClass in content.text)
# print("url in content=", url in content.text)

<div class="authors"><span class="descriptor">Authors:</span><a href="https://arxiv.org/search/cs?searchtype=author&amp;query=Betley,+J" rel="nofollow">Jan Betley</a>, <a href="https://arxiv.org/search/cs?searchtype=author&amp;query=Tan,+D" rel="nofollow">Daniel Tan</a>, <a href="https://arxiv.org/search/cs?searchtype=author&amp;query=Warncke,+N" rel="nofollow">Niels Warncke</a>, <a href="https://arxiv.org/search/cs?searchtype=author&amp;query=Sztyber-Betley,+A" rel="nofollow">Anna Sztyber-Betley</a>, <a href="https://arxiv.org/search/cs?searchtype=author&amp;query=Bao,+X" rel="nofollow">Xuchan Bao</a>, <a href="https://arxiv.org/search/cs?searchtype=author&amp;query=Soto,+M" rel="nofollow">Martín Soto</a>, <a href="https://arxiv.org/search/cs?searchtype=author&amp;query=Labenz,+N" rel="nofollow">Nathan Labenz</a>, <a href="https://arxiv.org/search/cs?searchtype=author&amp;query=Evans,+O" rel="nofollow">Owain Evans</a></div>

authors = author.split(" and ")
print(authors)

for a in authors:
    print(f"{a} in content=", a in content.text)