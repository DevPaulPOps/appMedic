from models.signalement import Signalement


class SignalementService:
    def __init__(self, repository):
        self.repository = repository

    def update_signalement(self, signalement_id, pseudo, code_cip):
        signalement = Signalement(pseudo, code_cip)
        update_data = signalement.to_dict()
        modified = self.repository.update(signalement_id, update_data)
        if modified == 0:
            raise ValueError("Aucun signalement n'a été modifié.")
        return modified

    def created_signalement(self, signalement_id, pseudo, code_cip):
        signalement = Signalement(pseudo, code_cip)
        created_data = signalement.to_dict()
        modified = self.repository.update(signalement_id, created_data)
        if modified == 0:
            raise ValueError("Aucun signalement n'a été modifié.")
        return modified