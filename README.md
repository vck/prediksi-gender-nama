# What

PoC of gender identification based on name (kind of yucky, I know)

# Why

Because, I thought machine learning was fun. So this repository was made.
For serious sake, I want a tool that can tell me if Vicky is reffer to which gender,
but when I think about it, it's kind of lame, because the more M data that I fed to the model, the more likely
the model results higher probability of Vicky being M, vice versa. But the thing here is, as name mostly consist of more
than two parts, i.e first name, middle name, and last name, these feature can tell if Vicky Nitinegoro or Vicky Burky is
a male or female. All I need is a good FEATURE ENGINEERING. No, ALL WE NEED, IS A GOOD FEATURE ENGINEERING!

see my lame blog post here (spoiler, I didn't use that megabytes size cover image on this medium post, peace!)
[medium](https://medium.com/@dasta/bisakah-mesin-membedakan-gender-dari-sebuah-nama-f081c656fc31)


# Setup



* pasang [anaconda](https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh)

* `source ~/anaconda3/bin/activate`
* `python server.py`
* antar muka web nya bisa kamu kunjungi di localhost:5000/ 


# TODO

- Feature engineering FTW
- Better models, use pytorch/tensorflow as it's fancier!
- Add model metrics
- Update web UI

# License

Licensed under Do What The Fuck You Want To Public License
