from pydantic import BaseModel, Field

class Vendor(BaseModel):
    vendor_id: int
    vendor_name: str = Field(..., max_length=50, description="Vendor name cannot exceed 50 characters.")
    category: str = Field(..., max_length=30, description="Category cannot exceed 30 characters.")
    years_in_business: int = Field(..., ge=0, description="Years in business must be non-negative.")
    contact: str = Field(..., pattern=r'^\+?\d{10,15}$', description="Contact must be 10-15 digits.")
    status: str = Field(..., pattern=r'^(active|inactive)$', description="Status must be 'active' or 'inactive'.")
