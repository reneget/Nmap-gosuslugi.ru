// API клиент для подключения к database и main_server
class API {
    constructor() {
        this.databaseUrl = 'http://localhost:8000'; // database API
        this.mainServerUrl = 'http://localhost:8001'; // main_server API
    }

    // Database API методы
    async getAllUsers() {
        try {
            const response = await fetch(`${this.databaseUrl}/user/get/all/users`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Ошибка получения пользователей:', error);
            throw error;
        }
    }

    async getUserById(userId) {
        try {
            const response = await fetch(`${this.databaseUrl}/user/get/user/${userId}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Ошибка получения пользователя:', error);
            throw error;
        }
    }

    async createUser(userData) {
        try {
            const response = await fetch(`${this.databaseUrl}/user/create/user`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(userData)
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Ошибка создания пользователя:', error);
            throw error;
        }
    }

    async updateUser(userId, userData) {
        try {
            const response = await fetch(`${this.databaseUrl}/user/update/user/${userId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(userData)
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Ошибка обновления пользователя:', error);
            throw error;
        }
    }

    async deleteUser(userId) {
        try {
            const response = await fetch(`${this.databaseUrl}/user/delete/user/${userId}`, {
                method: 'DELETE'
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Ошибка удаления пользователя:', error);
            throw error;
        }
    }

    async getUserKeyProperties(userId) {
        try {
            const response = await fetch(`${this.databaseUrl}/user/get/key/properties/user/${userId}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Ошибка получения свойств ключа:', error);
            throw error;
        }
    }

    // Main Server API методы
    async checkPassword(userId, key, entropy) {
        try {
            const response = await fetch(`${this.mainServerUrl}/server/chek/password`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    user_id: userId,
                    key: key,
                    entropy: entropy
                })
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Ошибка проверки пароля:', error);
            throw error;
        }
    }

    async adminLogin(username, password) {
        try {
            const response = await fetch(`${this.mainServerUrl}/server/admin/login`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: username,
                    password: password
                })
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Ошибка входа администратора:', error);
            throw error;
        }
    }
}

// Создаем глобальный экземпляр API
window.api = new API();
