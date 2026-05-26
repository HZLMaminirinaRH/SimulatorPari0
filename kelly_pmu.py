import os

def calculer_kelly(cote, proba):
    """Calcule la mise optimale selon le critère de Kelly."""
    b = cote - 1
    p = proba / 100
    q = 1 - p
    if b <= 0: return 0
    f_star = (b * p - q) / b
    return max(0, f_star)

def logger_resultat(cote, proba, mise_reelle, capital):
    """Enregistre l'analyse dans le dossier Downloads de votre Android."""
    log_path = os.path.expanduser("~/storage/downloads/log_session_ia.txt")
    entree = f"\n[KELLY] Cote: {cote} | Proba: {proba}% | Mise suggérée: {mise_reelle:.2f} (Cap: {capital})"
    try:
        with open(log_path, "a") as f:
            f.write(entree)
        print(f"✅ Analyse enregistrée dans : {log_path}")
    except:
        print("⚠️ Erreur : Vérifiez l'accès au stockage (termux-setup-storage).")

def main():
    print("--- CALCULATEUR CRITÈRE DE KELLY ---")
    try:
        capital = float(input("Capital disponible (ex: 101100) : "))
        cote = float(input("Cote du pari (ex: 3.5) : "))
        proba = float(input("Probabilité estimée en % (ex: 40) : "))

        f_star = calculer_kelly(cote, proba)

        if f_star > 0:
            # On applique la stratégie 'Fractional Kelly' (50%) pour plus de sécurité
            mise_suggeree = (f_star * 0.5) * capital
            print(f"\n💡 AVANTAGE DÉTECTÉ !")
            print(f"Mise suggérée (50% Kelly) : {mise_suggeree:.2f}")
            print(f"Part du capital : {(f_star * 0.5) * 100:.2f}%")
            logger_resultat(cote, proba, mise_suggeree, capital)
        else:
            print("\n❌ AUCUN AVANTAGE. Ne misez pas sur ce pari.")
            logger_resultat(cote, proba, 0, capital)
            
    except ValueError:
        print("Erreur : Veuillez entrer uniquement des chiffres.")

if __name__ == "__main__":
    main()
