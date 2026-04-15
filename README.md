# koodiklinikka-emoji

Tämä repo sisältää Koodiklinikan Slackissa käytössä olevat emojit.
Emojeita on ajan myötä lisännyt eri ihmiset, ja niitä on tullut eri lähteistä,
joten niiden laatu sekä lisenssitiedot vaihtelevat paljon.

## Päivittäminen

1. Käytä esim. [akx:n slack-emoji -työkaluja](https://github.com/akx/slack-emoji), jotta saat kansiollisen emojeja.
2. Poista (ei `git rm`, vaan ihan worktreestä vaan) kaikki nykyiset emojit.
3. Aja `python3 _scripts/update.py --source ../step-1-kansion-nimi`
4. Aja `python3 _scripts/gen_index.py`
5. `git add .`
6. `git commit -m "Päivitys"`
