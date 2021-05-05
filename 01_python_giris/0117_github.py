#region vscode_ile_github_kullanimiiiiii
r"""
Adım 1 → "git enable" seçili mi?
Manage → Settings → arama: "git enable" → seçili olduğuna emin olalım
Adım 2 → git client kurulu mu?
Source Control → Initialize Repository seçilemiyor ise kurulu değildir. "Install git" diyerek kuralım.
https://git-scm.com/
Adım 3 → Repo oluşturalım
https://github.com/ → Proje ile aynı isimde repo oluşturalım
https://github.com/azizbektas/VSCode-Ecodation-PC.git
Adım 4 → Vscode ile repoyu bağlamak için "Add Remote"
View → Comment Palette → arama: "Add Remote" 
Repository Url: "repo url'sini ekle" https://github.com/azizbektas/VSCode-Ecodation-PC.git
Remote Name: "remote ismi ekle" VSCode-Ecodation-PC
Adım 5 → Authenticaion/Authorization işlemi için kalıcı token oluştur.
https://github.com/settings/tokens → Generate New Token
Adım 6 → Authenticaion/Authorization işlemi için Account yöntemi ile geçici token oluştur
Turn on Settings Sync → Turn on → Sign in → Github → Authorized Github → VSCode Aç
Adım 8 → Stage All Changes
Commit etmeden önce değişikliklerin üzerinde sağ tıklayıp stage yapıyoruz
Adım 7 → İlk gönderimde yada değişiklik anında her gönderim için Commit and Push yapılmalı
Views and More Actions → Commit | Yada | Source Control → Commit buton → Commit'e Bir İsim Ver "060321-2330"
Views and More Actions → Push | Yada | Status Bar'daki → Synchronize Changes buton, Login İçin Token Gir 
Adım 8 → Olurda Commit anında terminalde aşağıdaki gibi bir hata alırsanız
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
"C:\Program Files\Git>" dizini altında github bilgilerini sırayla girin
C:\Program Files\Git> git config --global user.email "you@example.com"
C:\Program Files\Git> git config --global user.name "Your Name"
"""
#endregion